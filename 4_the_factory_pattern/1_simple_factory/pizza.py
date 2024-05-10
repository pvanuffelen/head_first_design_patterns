from abc import ABC, abstractmethod


class Pizza(ABC):

    def __init__(self):
        self.name = None,
        self.dough = None
        self.sauce = None
        self.toppings = list()

    def prepare(self):
        print(f"Preparing {self.name}")
        print(f"Tossing dough...")
        print(f"Adding sauce...")
        print(f"Adding toppings:")
        for i in self.toppings:
            print(f" {i}")

    def bake(self):
        print("Bake for 25 minutes at 350 degrees Fahrenheit")

    def cut(self):
        print("Cutting pizza in diagonal slices")

    def box(self):
        print("Place pizza in official PizzaStore box")

    def get_name(self):
        return self.name
