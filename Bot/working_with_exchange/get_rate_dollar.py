from abc import ABC, abstractmethod
import requests


class BaseExchange(ABC):

    @abstractmethod
    def get_exchange_rate(self) -> str:
        pass


class DollarExchangeFixer(BaseExchange):

    def __init__(self, currency: str, to: str, api_key: str):
        self.currency = currency
        self.to = to
        self.api_key = api_key

    def get_exchange_rate(self) -> float:
        url = f"http://data.fixer.io/api/latest?access_key={self.api_key}&symbols={self.currency},{self.to}&format=1"
        data = requests.get(url)
        data.raise_for_status()
        response = data.json()
        if response["success"]:
            rates = response["rates"]
            exchange_rate = rates.get(self.to)
            return exchange_rate
