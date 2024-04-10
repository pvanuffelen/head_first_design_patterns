from observer import Observer
from display_element import DisplayElement
from weather_data import WeatherData
from typing import List


class StatisticsDisplay(Observer, DisplayElement):

    def __init__(self, weather_data: WeatherData):
        self.weather_data: WeatherData = weather_data
        self.weather_data.register_observer(self)  # register the display as an observer
        self.temperature: float = 0  # degrees fahrenheit
        self.humidity: float = 0  # percentage
        self.pressure: float = 0  # psi
        self.historic_temperature: List[float] = []

    def update(self):
        self.temperature = self.weather_data.get_temperature()
        self.humidity = self.weather_data.get_humidity()
        self.historic_temperature.append(self.temperature)
        self.display()

    def display(self):
        average_temperature = sum(self.historic_temperature) / len(self.historic_temperature)
        maximum_temperature = max(self.historic_temperature)
        minimum_temperature = min(self.historic_temperature)
        print(f"Avg/Max/Min temperature = {average_temperature}/{maximum_temperature:.1f}/{minimum_temperature:.1f}")
