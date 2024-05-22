from subject import Subject
from observer import Observer
from typing import List


class WeatherData(Subject):
    """The weather data class, which implements the Subject interface"""

    def __init__(self):
        self.observers: List[Observer] = []
        self.temperature: float = 0  # degrees fahrenheit
        self.humidity: float = 0  # percentage
        self.pressure: float = 0  # psi

    def register_observer(self, observer: Observer):
        """Method that implements the register_observer method, by adding an observer to the list of observers"""
        self.observers.append(observer)

    def remove_observer(self, observer: Observer):
        """Method that implements the remove_observer method, by removing an observer from the list of observers"""
        self.observers.remove(observer)

    def notify_observers(self):
        """Method that implements the notify_observers method, tells all the observer about the state
        Because they are all Observers, we know they all implement update(), so we know how to notify them"""
        for observer in self.observers:
            observer.update()

    def measurements_changed(self):
        """Notify the observers when we get updated measurements from the Weather Station"""
        self.notify_observers()

    def set_measurements(self, temperature: float, humidity: float, pressure: float):
        """Setter method for all the states of the weather station"""
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurements_changed()

    def get_temperature(self) -> float:
        return self.temperature

    def get_humidity(self) -> float:
        return self.humidity

    def get_pressure(self) -> float:
        return self.pressure

    # other WeatherData methods here
