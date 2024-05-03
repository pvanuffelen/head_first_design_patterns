from pizza_store import PizzaStore


class NYStylePizzaStore(PizzaStore):

    def create_pizza(self, item: str):
        if item == "cheese":
            return NYStyleCheesePizza()
        elif item == "veggie":
            return NYVeggieStyleCheesePizza()
        elif item == "clam":
            return NYClamStyleCheesePizza()
        elif item == "pepperoni":
            return NYPepperoniStyleCheesePizza()
        else
            return None
