from abc import ABC, abstractmethod
from ingredients import Dough, Sauce, Veggies, Cheese, Pepperoni, Clams


class Pizza(ABC):

    def __init__(self):
        self.name: str = None,
        self.dough: Dough = None
        self.sauce: Sauce = None
        self.veggies: Veggies = None
        self.cheese: Cheese = None
        self.pepperoni: Pepperoni = None
        self.clam: Clams = None

    @abstractmethod
    def prepare(self):
        """Abstract prepare method, this is where we are going to collect the ingredients coming fo"""
        pass

    def bake(self):
        print("Bake for 25 minutes at 350 degrees Fahrenheit")

    def cut(self):
        print("Cutting pizza in diagonal slices")

    def box(self):
        print("Place pizza in official PizzaStore box")

    def set_name(self, name: str):
        self.name = name

    def get_name(self):
        return self.name

    def to_string(self) -> str:
        # code to print pizza here
        pass
