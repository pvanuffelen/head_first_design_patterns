from abc import ABC, abstractmethod
from typing import List


class Pizza(ABC):

    def __init__(self, name: str, dough: str, sauce: str, toppings: List[str]):
        self.name = name,
        self.dough = dough
        self.sauce = sauce
        self.toppings = toppings

    def prepare(self):
        print(f"Preparing {self.name}")
        print(f"Tossing dough...")
        print(f"Adding sauce...")
        print(f"Adding toppings:")
        for i in self.toppings:
            print(f" {i}")

    @staticmethod
    def bake():
        print("Bake for 25 minutes at 350 degrees Fahrenheit")

    @staticmethod
    def cut():
        print("Cutting pizza in diagonal slices")

    @staticmethod
    def box():
        print("Place pizza in official PizzaStore box")

    def get_name(self):
        return self.name
