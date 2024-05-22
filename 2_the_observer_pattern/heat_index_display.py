from observer import Observer
from display_element import DisplayElement
from weather_data import WeatherData


def calculate_heat_index(temperature: float, humidity: float) -> float:
    T = temperature
    RH = humidity
    heat_index = (
        16.923
        + (0.185212 * T)
        + (5.37941 * RH)
        - (0.100254 * T * RH)
        + (0.00941695 * (T * T))
        + (0.00728898 * (RH * RH))
        + (0.000345372 * (T * T * RH))
        - (0.000814971 * (T * RH * RH))
        + (0.0000102102 * (T * T * RH * RH))
        - (0.000038646 * (T * T * T))
        + (0.0000291583 * (RH * RH * RH))
        + (0.00000142721 * (T * T * T * RH))
        + (0.000000197483 * (T * RH * RH * RH))
        - (0.0000000218429 * (T * T * T * RH * RH))
        + 0.000000000843296 * (T * T * RH * RH * RH)
    ) - 0.0000000000481975 * (T * T * T * RH * RH * RH)

    return heat_index


class HeatIndexDisplay(Observer, DisplayElement):

    def __init__(self, weather_data: WeatherData):
        self.weather_data: WeatherData = weather_data
        self.weather_data.register_observer(self)  # register the display as an observer
        self.temperature: float = 0  # degrees fahrenheit
        self.humidity: float = 0  # percentage
        self.pressure: float = 0  # psi
        self.heat_index: float = 0  # degrees fahrenheit

    def update(self):
        self.temperature = self.weather_data.get_temperature()
        self.humidity = self.weather_data.get_humidity()
        self.heat_index = calculate_heat_index(self.temperature, self.humidity)
        self.display()

    def display(self):
        print(f"Heat index is {self.heat_index:.5f}")
