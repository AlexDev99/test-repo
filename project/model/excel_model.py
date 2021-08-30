from project.model.fact import Fact
from project.model.forecast import Forecast


class ExcelModel:
    __name_company: str
    __fact: Fact
    __forecast: Forecast

    def __init__(self, name_company):
        self.__name_company = name_company

    @property
    def name_company(self):
        return self.__name_company

    @property
    def fact(self):
        return self.__fact

    @fact.setter
    def fact(self, fact: Fact):
        self.__fact = fact

    @property
    def forecast(self):
        return self.__forecast

    @forecast.setter
    def forecast(self, forecast: Forecast):
        self.__forecast = forecast
