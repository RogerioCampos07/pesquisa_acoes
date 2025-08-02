import os

import requests
from dotenv import load_dotenv

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
        if response.status_code == 200:
            return response.json()
        else:
            return None


client = SearchTicker()
vale = client.search_ticker("VALE3.SA")
print(vale)
