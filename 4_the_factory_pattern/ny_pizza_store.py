from pizza_store import PizzaStore
from ny_pizza_ingredient_factory import NYPizzaIngredientFactory
from cheese_pizza import CheesePizza
from clam_pizza import ClamPizza
from veggie_pizza import VeggiePizza
from pepperoni_pizza import PepperoniPizza

class NYStylePizzaStore(PizzaStore):

    def create_pizza(self, item: str):
        pizza = None
        ingredient_factory = NYPizzaIngredientFactory()
        if item == "cheese":
            pizza = CheesePizza(ingredient_factory)
            pizza.set_name("New York Style Cheese Pizza")
        elif item == "veggie":
            pizza = VeggiePizza(ingredient_factory)
            pizza.set_name("New York Style Veggie Pizza")
        elif item == "clam":
            pizza = ClamPizza(ingredient_factory)
            pizza.set_name("New York Style Clam Pizza")
        elif item == "pepperoni":
            pizza = PepperoniPizza(ingredient_factory)
            pizza.set_name("New York Style Pepperoni Pizza")

        return pizza
