import os
from datetime import datetime

import requests
from dotenv import load_dotenv
from loguru import logger

load_dotenv()


class SearchTicker:
    def __init__(self):
        self.__base_url = "https://brapi.dev/api/quote/"
        self._autenticator = self.autenticator()

    def autenticator(self):
        token = os.getenv("BRAPI_API_KEY")
        headers = {"Authorization": f"Bearer {token}"}
        return headers

    def search_ticker(self, ticker):
        url = f"{self.__base_url}{ticker}"
        response = requests.get(url, headers=self._autenticator)
        if response.status_code != 200:
            return logger.error("Não foi possivel encontrar o ticker")

        return response.json()

    def get_info_ticker(self, ticker):
        now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        data = self.search_ticker(ticker)
        ticker = {}
        ticker["symbol"] = data["results"][0]["symbol"]
        ticker["name"] = data["results"][0]["longName"]
        ticker["price"] = data["results"][0]["regularMarketPrice"]
        ticker["date"] = data["date"] = now

        return ticker
