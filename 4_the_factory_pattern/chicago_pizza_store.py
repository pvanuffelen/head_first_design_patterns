from pizza_store import PizzaStore
# from ny_pizza_ingredient_factory import NYPizzaIngredientFactory
from cheese_pizza import CheesePizza
from clam_pizza import ClamPizza
from veggie_pizza import VeggiePizza
from pepperoni_pizza import PepperoniPizza


class ChicagoStylePizzaStore(PizzaStore):

    def create_pizza(self, item: str):
        if item == "cheese":
            return ChicagoStyleCheesePizza()
        elif item == "veggie":
            return ChicagoVeggieStyleCheesePizza()
        elif item == "clam":
            return ChicagoClamStyleCheesePizza()
        elif item == "pepperoni":
            return ChicagoPepperoniStyleCheesePizza()
        else:
            return None
