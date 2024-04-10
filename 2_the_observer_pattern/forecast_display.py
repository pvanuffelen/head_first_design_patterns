from observer import Observer
from display_element import DisplayElement
from weather_data import WeatherData


class ForecastDisplay(Observer, DisplayElement):

    def __init__(self, weather_data: WeatherData):
        self.weather_data: WeatherData = weather_data
        self.weather_data.register_observer(self)  # register the display as an observer
        self.current_pressure: float = 29.9  # psi
        self.last_pressure: float = 0

    def update(self) -> None:
        self.last_pressure = self.current_pressure
        self.current_pressure = self.weather_data.get_pressure()
        self.display()

    def display(self):
        if self.last_pressure > self.current_pressure:
            forecast = f"Watch out for cooler, rainy weather"
        elif self.last_pressure < self.current_pressure:
            forecast = f"Improving weather on the way!"
        else:
            forecast = f"More of the same"
        print(f"Forecast: " + forecast)
