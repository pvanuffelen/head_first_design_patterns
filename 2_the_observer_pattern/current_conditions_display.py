from observer import Observer
from display_element import DisplayElement
from weather_data import WeatherData


class CurrentConditionsDisplay(Observer, DisplayElement):

    def __init__(self, weather_data: WeatherData):
        self.weather_data: WeatherData = weather_data
        self.weather_data.register_observer(self)  # register the display as an observer
        self.temperature: float = 0  # degrees fahrenheit
        self.humidity: float = 0  # percentage
        self.pressure: float = 0  # psi

    def update(self, temperature: float, humidity: float, pressure: float):
        self.temperature = temperature
        self.humidity = humidity
        self.display()

    def display(self):
        print(f"Current conditions: {self.temperature} F degrees and {self.humidity} % humidity")
