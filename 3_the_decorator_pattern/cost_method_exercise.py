"""Note that this is all pseudocode, just to get an idea of how to solve the problem"""

from abc import ABC, abstractmethod


class Beverage(ABC):
    def __init__(self):
        self.toppings: bool = False

    @abstractmethod
    def cost(self) -> float:
        cost_toppings = 0.50 * self.toppings
        return cost_toppings


class DarkRoast(Beverage):

    def cost(self) -> float:
        mycost = self.cost() + 1
        return mycost
