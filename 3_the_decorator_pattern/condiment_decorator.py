from abc import abstractmethod
from beverage import Beverage


class CondimentDecorator(Beverage):

    def __init__(self, beverage: Beverage):
        """

        :type beverage: Beverage
        """
        self.beverage = beverage  # the Beverage that each Decorator will be wrapping

    @abstractmethod
    def get_description(self):
        """Every condiment needs to reimplement the get_description method"""
        pass
