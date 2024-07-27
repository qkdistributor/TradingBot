import pandas as pd

from td.client import TDClient
from td.utils import milliseconds_since_epoch

from datetime import datetime, time, timezone

from typing import List, Dict, Union

#Robot object represents user interacting with market
class pyRobot():
    def __init__(self, client_id: str, redirect_uri: str, credentials_path: str = None, trading_account: str = None) -> None:
        self.trading_account = trading_account
        self.client_id = client_id
        self.redirect_uri = redirect_uri
        self.credentials_path = credentials_path
        self.session: TDClient = self._create_session()
        self.trades: dict = {}
        self.historical_prices: dict = {}
        self.stock_frame = None
    
    #Create trading session
    def _create_session(self) -> TDClient:
        td_client = TDClient(
            td_client=self.client_id,
            redirect_uri=self.redirect_uri,
            credentials_path=self.credentials_path
        )

        #login to session
        td_client.login()

        return td_client
    
    #is current time pre-market
    @property
    def pre_market_open(self) -> bool:
        pre_market_start_time = datetime.now().replace(hour = 12, minute = 00, second = 00, tzinfo = timezone.utc).timestamp()
        market_start_time = datetime.now().replace(hour = 13, minute = 30, second = 00, tzinfo = timezone.utc).timestamp()
        right_now = datetime.now().replace(tzinfo=timezone.utc).timestamp()

        if market_start_time >= right_now >= pre_market_start_time:
            return True
        else:
            return False


    #is current time post market
    @property
    def post_market_open(self) -> bool:
        post_market_end_time = datetime.now().replace(hour = 22, minute = 30, second = 00, tzinfo = timezone.utc).timestamp()
        market_end_time = datetime.now().replace(hour = 20, minute = 00, second = 00, tzinfo = timezone.utc).timestamp()
        right_now = datetime.now().replace(tzinfo=timezone.utc).timestamp()

        if post_market_end_time >= right_now >= market_end_time:
            return True
        else:
            return False

    #is current time during market hours
    @property
    def regular_markets_open(self) -> bool:
        market_start_time = datetime.now().replace(hour = 13, minute = 30, second = 00, tzinfo = timezone.utc).timestamp()
        market_end_time = datetime.now().replace(hour = 20, minute = 00, second = 00, tzinfo = timezone.utc).timestamp()
        right_now = datetime.now().replace(tzinfo=timezone.utc).timestamp()

        if market_end_time >= right_now >= market_start_time:
            return True
        else:
            return False
        
    def create_portfolio(self):
        pass

    def create_trade(self):
        pass

    def create_stock_frame(self):
        pass

    def grab_current_quotes(self) -> dict:
        pass

    def grab_historical_prices(self) -> List[Dict]:
        pass