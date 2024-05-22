from abc import ABC, abstractmethod


class Beverage(ABC):
    """The abstract class all beverages and toppings inherit from"""

    def __init__(self):
        self.description: str = "Unknown Beverage"

    def get_description(self):
        return self.description

    @abstractmethod
    def cost(self):
        """Abstract method, so all subclasses need to implement this method self"""
        pass
