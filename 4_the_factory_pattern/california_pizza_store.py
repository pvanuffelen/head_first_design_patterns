from pizza_store import PizzaStore


class CaliforniaStylePizzaStore(PizzaStore):

    def create_pizza(self, item: str):
        if item == "cheese":
            return CaliforniaStyleCheesePizza()
        elif item == "veggie":
            return CaliforniaVeggieStyleCheesePizza()
        elif item == "clam":
            return CaliforniaClamStyleCheesePizza()
        elif item == "pepperoni":
            return CaliforniaPepperoniStyleCheesePizza()
        else:
            return None
