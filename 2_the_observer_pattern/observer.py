from abc import ABCMeta, abstractmethod


class Observer(metaclass=ABCMeta):
    """Observer class to act as the observer interface. All observers implement this interface."""
    @abstractmethod
    def update(self, temp: float, humidity: float, pressure: float) -> None:
        """Method that all observers must implement. Takes all the state values as an input"""
        raise NotImplementedError
