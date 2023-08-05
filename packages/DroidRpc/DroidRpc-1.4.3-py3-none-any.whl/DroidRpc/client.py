# Python client for connecting to LORA Technologies' bot services

__author__ = "LORA Technologies"
__email__ = "asklora@loratechai.com"

from ast import Try
from io import BytesIO
from typing import Optional, List, Generator, Union
import grpc
import pandas as pd

from .grpc_interface import bot_pb2_grpc, bot_pb2
from datetime import datetime
from .converter import (
    datetime_to_timestamp,
    array_to_bytes,
    bytes_to_array,
    protobuf_to_dict,
)
from .dataclasses import create_inputs, hedge_inputs, stop_inputs
import math
import numpy as np
import json
import warnings
from timeit import default_timer as timer
from datetime import timedelta


# TODO use pydantic dataclass to validate field types.

class Client:

    batch_size = 400

    def __init__(self,
                 address: str = "guardian",
                 port: str = "50065",
                 batch_size: int = None):
        self.address = address
        self.port = port
        # TODO: Use a secure channel because this is external facing
        self.channel = grpc.insecure_channel(self.address + ":" + self.port)
        self.droid = bot_pb2_grpc.DroidStub(
            self.channel
        )  # This one contains the bistream
        if batch_size is not None:
            self.batch_size = batch_size

    def __string_to_datetime(self, date: str):
        date = datetime.strptime(date, "%Y-%m-%d")
        time = datetime.now().time()

        date_class = datetime_to_timestamp(datetime.combine(date, time))
        return date_class

    def create_bot(
            self,
            ticker: str,
            spot_date: str,
            bot_id: str,
            investment_amount: float,
            ask_price: float,
            bid_price: float,
            margin: Optional[float] = None,
            fraction: Optional[bool] = None,
            multiplier_1: Optional[float] = None,
            multiplier_2: Optional[float] = None,
    ) -> dict:
        """
        Create a single bot
        Docs: https://loratechai.atlassian.net/wiki/spaces/DROID/pages/1077838028/DROID+Batch+Data+Flow#Properites

        Args:
            ticker (str): Ticker ID in our universe (not necessarily RIC).
            spot_date (str): Bot start date (YYYY-MM-DD).
            bot_id (str): Unique ID for the bot (e.g. "UNO_OTM_003846").
            investment_amount (float): Initial investment amount.
            ask_price (float): Current ask price.
            bid_price (float): Current bid price.
            margin (Optional[float], optional): Margin ratio (1 = no margin). Defaults to None.
            fraction (Optional[bool], optional): Whether fractional shares are allowed. Defaults to None.
            multiplier_1 (Optional[float], optional): Multiplier for target price level 1. Defaults to None.
            multiplier_2 (Optional[float], optional): Multiplier for target price level 2, must be > multiplier_2. Defaults to None.

        Returns:
            dict: Status of new bot, including hedge shares and price levels.
        """
        # The non-batch version of create_bots is not maintained on the server side.
        # Therefore we use the batch version with list of length 1 for backwards compatibility.

        data = {
            'ticker': ticker,
            'spot_date': spot_date,
            'bot_id': bot_id,
            'investment_amount': investment_amount,
            'ask_price': ask_price,
            'bid_price': bid_price,
            'margin': margin,
            'fraction': fraction,
        }
        # Annoyingly, the PD batch create function doesnt let you pass in None values
        # so we have to do this separately
        if multiplier_1 is not None:
            data['multiplier_1'] = multiplier_1
        if multiplier_2 is not None:
            data['multiplier_2'] = multiplier_2

        df = pd.Series(data).to_frame().T
        response = self.create_bots(df)
        response = next(response)
        response = response.to_dict()
        response = {key: response[key][0] for key in response.keys()}
        return response

    def __create_bots_generator(self, input_matrix: np.ndarray):
        """
        Generator function to be passed to the create_bots() gRPC bistream function.
        Splits a matrix of inputs into sub-batches and streams these sub-batches to Droid.

        Args:
            input_matrix (np.array(9,1)): List of inputs for each bot. The format is each row corresponds to the BatchCreate protobuf message.
        """

        # Split input matrix into smaller batches
        splits = math.ceil(input_matrix.shape[1] / self.batch_size)
        input_matrix = np.array_split(input_matrix, splits, axis=1)

        for batch in input_matrix:
            try:
                message = bot_pb2.BatchCreate(
                    ticker=array_to_bytes(batch[0].astype(str)),
                    spot_date=array_to_bytes(batch[1].astype(np.datetime64)),
                    bot_id=array_to_bytes(batch[2].astype(str)),
                    investment_amount=array_to_bytes(batch[3].astype(float)),
                    ask_price=array_to_bytes(batch[4].astype(float)),
                    bid_price=array_to_bytes(batch[5].astype(float)),
                    margin=array_to_bytes(batch[6].astype(float)),
                    fraction=array_to_bytes(batch[7].astype(bool)),
                    multiplier_1=array_to_bytes(batch[8].astype(float)),
                    multiplier_2=array_to_bytes(batch[9].astype(float)),
                )
            except TypeError as e:
                print(e)
            except Exception as e:
                print(e)
            # print(message.__sizeof__())

            yield message

    def __batch_response_generator(self, responses):
        """
        Generator function that wraps the gRPC bistream generator to convert
        bytes into numpy arrays

        Args:
            responses (generator obj): The gRPC bistream generator obj.
        """
        for response in responses:
            try:
                output = {
                    field: bytes_to_array(value)
                    for (field, value) in protobuf_to_dict(response).items()
                }
                output = np.array([row[1] for row in output.items()])
                output = np.rot90(output)
                # print(output)
            except TypeError as e:
                print(e)
            except Exception as e:
                print(e)
            yield output

    def create_bots(
            self,
            create_inputs: Union[List[create_inputs],
                                 Generator,
                                 pd.DataFrame],
            input_type: str = "list",
    ):
        """
        Returns a list of bots as dictionaries.

        Args:
            create_inputs (List[create_inputs]): Inputs for bot create.
        Kwargs:
            input_type (str): Type of accepted inputs. Defaults to 'list'.
                list : List of create_inputs dataclass objs
                generator : Generator obj that yields lists of inputs

        Returns:
            Generator: Generator of responses from Droid.
        """
        if isinstance(create_inputs, list):
            # Convert the inputs into numpy arrays
            # print(create_inputs)
            start = timer()
            input_matrix = np.empty([1, 10])
            for i in create_inputs:
                arr = np.array(
                    [
                        [
                            # make sure this list consistent with bot.proto
                            i.ticker,
                            np.datetime64(i.spot_date),
                            i.bot_id,
                            i.investment_amount,
                            i.ask_price,
                            i.bid_price,
                            i.margin,
                            i.fraction,
                            i.multiplier_1,
                            i.multiplier_2,
                        ]
                    ]
                )
                input_matrix = np.concatenate(
                    (input_matrix, arr)
                )  # TODO: Fix crazy memory allocations
            input_matrix = np.delete(input_matrix, 0, 0)
            print(
                f"Total Numpy Conversion time: {timedelta(seconds=(timer() - start))}")

            # Rotate matrix
            input_matrix = np.rot90(input_matrix, k=-1)

            return self.__batch_response_generator(
                self.droid.CreateBots(
                    self.__create_bots_generator(input_matrix))
            )

        elif isinstance(create_inputs, pd.DataFrame):
            return self.__output_stream(
                self.droid.CreateBots(
                    self.__input_stream(create_inputs, bot_pb2.BatchCreate)
                )
            )
        # if isinstance(input_type, list):
        #     # TODO: This is so that we can pipeline bot creation
        #     return self.droid.CreateBots(create_inputs)

        else:
            raise ValueError(f"{type(create_inputs)} is not a valid type")

    def __output_stream(self, responses: dict) -> pd.DataFrame:
        """
        convert grpc byte response into dataframe
        """
        for i in responses:
            output = {field: bytes_to_array(value)
                      for (field, value) in protobuf_to_dict(i).items()}
            output = pd.DataFrame(output)
            yield output.convert_dtypes()

    def __input_stream(self, inputs: pd.DataFrame, serializer):
        """
        convert dataframe inputs into byte -> serialized input for grpc
        """
        n_batch = np.ceil(len(inputs) / self.batch_size)
        chunks = np.array_split(inputs, n_batch)
        for i in chunks:
            byte_input = {
                col: array_to_bytes(i[col].to_numpy().astype(str))
                if "date" not in col
                else array_to_bytes(pd.to_datetime(i[col]).dt.date
                                    .to_numpy().astype(str))
                for col in i}
            serialized_input = serializer(**byte_input)
            yield serialized_input

    def hedge(
            self,
            ticker: str,
            spot_date: str,
            bot_id: str,
            investment_amount: float,
            ask_price: float,
            bid_price: float,
            margin: float,
            fraction: bool,
            total_bot_share_num: float,
            expire_date: str,
            price_level_1: float,
            price_level_2: float,
            last_hedge_delta: Optional[float] = None,
            last_share_num: Optional[float] = None,
            bot_cash_balance: Optional[float] = None,
    ) -> dict:
        """
        Returns a dictionary of hedge results for a single bot.
        Docs: https://loratechai.atlassian.net/wiki/spaces/DROID/pages/1077838028/DROID+Batch+Data+Flow#Properites

        Args:
            ticker (str): Ticker ID in our universe (not necessarily RIC).
            spot_date (str): Bot start date (YYYY-MM-DD).
            bot_id (str): Unique ID for the bot (e.g. "UNO_OTM_003846").
            investment_amount (float): Initial investment amount.
            ask_price (float): Current ask price.
            bid_price (float): Current bid price.
            margin (Optional[float], optional): Margin ratio (1 = no margin). Defaults to None.
            fraction (Optional[bool], optional): Whether fractional shares are allowed. Defaults to None.
            total_bot_share_num (float): Maximum number of holdable shares (decided at bot creation).
            expire_date (str): Bot end date, i.e. holding period end.
            price_level_1 (float): Value depends on the bot type. Refer to docs.
            price_level_2 (float): Value depends on the bot type. Refer to docs.
            last_hedge_delta (Optional[float], optional): Current hedging delta. Defaults to None.
            last_share_num (Optional[float], optional): Number of shares in position. Defaults to None.
            bot_cash_balance (Optional[float], optional): Cash balance in bot position, negative value implied using margin. Defaults to None.

        Returns:
            dict: Dictionary of hedge results.
        """
        # The non-batch version of hedge_bots is not maintained on the server side.
        # Therefore we use the batch version with list of length 1 for backwards compatibility.
         
        
        data = {
            'ticker': ticker,
            'spot_date': spot_date,
            'bot_id': bot_id,
            'investment_amount': investment_amount,
            'ask_price': ask_price,
            'bid_price': bid_price,
            'margin': margin,
            'fraction': fraction,
            'total_bot_share_num': total_bot_share_num,
            'expire_date': expire_date,
            'price_level_1': price_level_1,
            'price_level_2': price_level_2,
            'last_hedge_delta': last_hedge_delta,
            'last_share_num': last_share_num,
            'bot_cash_balance': bot_cash_balance,
        }

        df = pd.Series(data).to_frame().T
        response = self.hedge_bots(df)
        response = next(response)
        response = response.to_dict()
        response = {key: response[key][0] for key in response.keys()}
        return response

    def __hedge_bots_generator(self, input_matrix: np.array):
        """
        Generator function to be passed to the hedge_bots() gRPC bistream function.
        Splits a matrix of inputs into sub-batches and streams these sub-batches to Droid.

        Args:
            input_matrix (np.array(9,1)): List of inputs for each bnot. The format is each row corresponds to the BatchHedge protobuf message.
        """

        # Split input matrix into smaller batches
        splits = math.ceil(input_matrix.shape[1] / self.batch_size)
        input_matrix = np.array_split(input_matrix, splits, axis=1)

        for batch in input_matrix:
            try:
                message = bot_pb2.BatchHedge(
                    ticker=array_to_bytes(batch[0].astype(str)),
                    spot_date=array_to_bytes(batch[1].astype(np.datetime64)),
                    bot_id=array_to_bytes(batch[2].astype(str)),
                    investment_amount=array_to_bytes(batch[3].astype(float)),
                    ask_price=array_to_bytes(batch[4].astype(float)),
                    bid_price=array_to_bytes(batch[5].astype(float)),
                    margin=array_to_bytes(batch[6].astype(float)),
                    fraction=array_to_bytes(batch[7].astype(bool)),
                    last_hedge_delta=array_to_bytes(batch[8].astype(float)),
                    last_share_num=array_to_bytes(batch[9].astype(float)),
                    total_bot_share_num=array_to_bytes(batch[10].astype(float)),
                    bot_cash_balance=array_to_bytes(batch[11].astype(float)),
                    expire_date=array_to_bytes(batch[12].astype(np.datetime64)),
                    price_level_1=array_to_bytes(batch[13].astype(float)),
                    price_level_2=array_to_bytes(batch[14].astype(float)),
                )
            except TypeError as e:
                print(e)
            except Exception as e:
                print(e)
            # print(message.__sizeof__())

            yield message

    def hedge_bots(
            self,
            hedge_inputs: Union[List[hedge_inputs], Generator, pd.DataFrame],
            input_type: str = "list",
    ):
        """
        Returns a list of bots as dictionaries.

        Args:
            hedge_inputs (List[hedge_inputs]): Inputs for bot creation.
        Kwargs:
            input_type (str): Type of accepted inputs. Defaults to 'list'.
                list : List of hedge_inputs dataclass objs
                generator : Generator obj that yields lists of inputs

        Returns:
            Generator: Generator of responses from Droid.
        """
        if isinstance(hedge_inputs, list):
            print("hedging")
            # Convert inputs into np.ndarrays
            input_matrix = np.empty([1, 22])
            for i in hedge_inputs:
                arr = np.array(
                    [
                        [
                            i.ticker,
                            i.spot_date,
                            i.bot_id,
                            i.investment_amount,
                            i.ask_price,
                            i.bid_price,
                            i.margin,
                            i.fraction,
                            i.last_hedge_delta,
                            i.last_share_num,
                            i.total_bot_share_num,
                            i.bot_cash_balance,
                            i.expire_date,
                            i.price_level_1,
                            i.price_level_2,
                        ]
                    ]
                )
                input_matrix = np.concatenate(
                    (input_matrix, arr)
                )  # TODO: Fix crazy memory allocations
            input_matrix = np.delete(input_matrix, 0, 0)

            # Rotate matrix
            input_matrix = np.rot90(input_matrix, k=-1)

            generator = self.__hedge_bots_generator(input_matrix)
            hedgeBots = self.droid.HedgeBots(generator)
            outputGenerator = self.__batch_response_generator(hedgeBots)
            return outputGenerator

        elif isinstance(hedge_inputs, pd.DataFrame):
            return self.__output_stream(
                self.droid.HedgeBots(
                    self.__input_stream(hedge_inputs, bot_pb2.BatchHedge)
                )
            )

        # elif input_type == "generator":
        #     return self.droid.HedgeBots(hedge_inputs)
        else:
            raise ValueError(f"{type(hedge_inputs)} is not a valid type")

    def stop(
            self,
            ticker: str,
            spot_date: str,
            bot_id: str,
            investment_amount: float,
            ask_price: float,
            bid_price: float,
            margin: float,
            fraction: bool,
            total_bot_share_num: float,
            expire_date: str,
            price_level_1: float,
            price_level_2: float,
            last_hedge_delta: Optional[float] = None,
            last_share_num: Optional[float] = None,
            bot_cash_balance: Optional[float] = None,
    ) -> dict:
        """
        Returns a dictionary of hedge results for a single bot.
        Docs: https://loratechai.atlassian.net/wiki/spaces/DROID/pages/1077838028/DROID+Batch+Data+Flow#Properites

        Args:
            ticker (str): Ticker ID in our universe (not necessarily RIC).
            spot_date (str): Bot start date (YYYY-MM-DD).
            bot_id (str): Unique ID for the bot (e.g. "UNO_OTM_003846").
            investment_amount (float): Initial investment amount.
            ask_price (float): Current ask price.
            bid_price (float): Current bid price.
            margin (Optional[float], optional): Margin ratio (1 = no margin). Defaults to None.
            fraction (Optional[bool], optional): Whether fractional shares are allowed. Defaults to None.
            total_bot_share_num (float): Maximum number of holdable shares (decided at bot creation).
            expire_date (str): Bot end date, i.e. holding period end.
            price_level_1 (float): Value depends on the bot type. Refer to docs.
            price_level_2 (float): Value depends on the bot type. Refer to docs.
            last_hedge_delta (Optional[float], optional): Current hedging delta. Defaults to None.
            last_share_num (Optional[float], optional): Number of shares in position. Defaults to None.
            bot_cash_balance (Optional[float], optional): Cash balance in bot position, negative value implied using margin. Defaults to None.

        Returns:
            dict: Dictionary of stop results.
        """
        # The non-batch version of hedge_bots is not maintained on the server side.
        # Therefore we use the batch version with list of length 1 for backwards compatibility.
         
        
        data = {
            'ticker': ticker,
            'spot_date': spot_date,
            'bot_id': bot_id,
            'investment_amount': investment_amount,
            'ask_price': ask_price,
            'bid_price': bid_price,
            'margin': margin,
            'fraction': fraction,
            'total_bot_share_num': total_bot_share_num,
            'expire_date': expire_date,
            'price_level_1': price_level_1,
            'price_level_2': price_level_2,
            'last_hedge_delta': last_hedge_delta,
            'last_share_num': last_share_num,
            'bot_cash_balance': bot_cash_balance,
        }

        df = pd.Series(data).to_frame().T
        response = self.stop_bots(df)
        response = next(response)
        response = response.to_dict()
        response = {key: response[key][0] for key in response.keys()}
        return response

    def __stop_bots_generator(
            self,
            input_matrix: np.ndarray,
    ):
        splits = math.ceil(input_matrix.shape[1] / self.batch_size)
        input_matrix = np.array_split(input_matrix, splits, axis=1)

        for batch in input_matrix:
            try:
                message = bot_pb2.BatchStop(
                    ticker=array_to_bytes(batch[0].astype(str)),
                    spot_date=array_to_bytes(batch[1].astype(np.datetime64)),
                    bot_id=array_to_bytes(batch[2].astype(str)),
                    investment_amount=array_to_bytes(batch[3].astype(float)),
                    ask_price=array_to_bytes(batch[4].astype(float)),
                    bid_price=array_to_bytes(batch[5].astype(float)),
                    margin=array_to_bytes(batch[6].astype(float)),
                    fraction=array_to_bytes(batch[7].astype(bool)),
                    last_hedge_delta=array_to_bytes(batch[8].astype(float)),
                    last_share_num=array_to_bytes(batch[9].astype(float)),
                    total_bot_share_num=array_to_bytes(batch[10].astype(float)),
                    bot_cash_balance=array_to_bytes(batch[11].astype(float)),
                    expire_date=array_to_bytes(batch[12].astype(np.datetime64)),
                    price_level_1=array_to_bytes(batch[13].astype(float)),
                    price_level_2=array_to_bytes(batch[14].astype(float)),
                )
            except TypeError as e:
                print(e)
            except Exception as e:
                print(e)

            yield message

    def stop_bots(
            self, stop_inputs: Union[List[stop_inputs], Generator, pd.DataFrame],
            input_type: str = "list"
    ):

        if isinstance(stop_inputs, list):
            # Convert the inputs into numpy arrays
            input_matrix = np.empty([1, 22])
            for i in stop_inputs:
                arr = np.array(
                    [
                        [
                            i.ticker,
                            i.spot_date,
                            i.bot_id,
                            i.investment_amount,
                            i.ask_price,
                            i.bid_price,
                            i.margin,
                            i.fraction,
                            i.last_hedge_delta,
                            i.last_share_num,
                            i.total_bot_share_num,
                            i.bot_cash_balance,
                            i.expire_date,
                            i.price_level_1,
                            i.price_level_2,
                        ]
                    ]
                )
                input_matrix = np.concatenate(
                    (input_matrix, arr)
                )  # TODO: Fix crazy memory allocations
            input_matrix = np.delete(input_matrix, 0, 0)

            input_matrix = np.rot90(input_matrix, k=-1)

            return self.__batch_response_generator(
                self.droid.StopBots(self.__stop_bots_generator(input_matrix))
            )

        elif isinstance(stop_inputs, pd.DataFrame):
            return self.__output_stream(
                self.droid.HedgeBots(
                    self.__input_stream(stop_inputs, bot_pb2.BatchStop)
                )
            )

        elif input_type == "generator":
            return self.droid.StopBots(create_inputs)

        else:
            raise ValueError(f"{input_type} is not a valid type")
