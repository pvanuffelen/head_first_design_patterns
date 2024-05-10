from abc import ABC
from ingredients import Dough, Sauce, Cheese, Veggies, Pepperoni, Clams


class PizzaIngredientFactory:

    def create_dough(self) -> Dough:
        raise NotImplementedError

    def create_sauce(self) -> Sauce:
        raise NotImplementedError

    def create_cheese(self) -> Cheese:
        raise NotImplementedError

    def create_veggies(self) -> Veggies:
        raise NotImplementedError

    def create_pepperoni(self) -> Pepperoni:
        raise NotImplementedError

    def create_clam(self) -> Clams:
        raise NotImplementedError
