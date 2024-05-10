from pizza_ingredient_factory import PizzaIngredientFactory
from ingredients import (Dough, Sauce, Cheese,Pepperoni, Clams, ThinCrustDough, MarinaraSauce, ReggianoCheese, Veggies,
                         SlicedPepperoni, FreshClams)

class NYPizzaIngredientFactory(PizzaIngredientFactory):

        def create_dough(self) -> Dough:
            return ThinCrustDough()

        def create_sauce(self) -> Sauce:
            return MarinaraSauce()

        def create_cheese(self) -> Cheese:
            return ReggianoCheese()

        def create_veggies(self) -> Veggies:
            return Veggies()

        def create_pepperoni(self) -> Pepperoni:
            return SlicedPepperoni()

        def create_clam(self) -> Clams:
            return FreshClams()
