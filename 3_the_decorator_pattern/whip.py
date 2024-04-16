from beverage import Beverage
from condiment_decorator import CondimentDecorator


class Whip(CondimentDecorator):

    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def get_description(self) -> str:
        return self.beverage.get_description() + ", Whip"

    def cost(self) -> float:
        return self.beverage.cost() + 0.10
