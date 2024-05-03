from pizza_store import PizzaStore
from chicago_cheese_pizza import ChicagoStyleCheesePizza


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
