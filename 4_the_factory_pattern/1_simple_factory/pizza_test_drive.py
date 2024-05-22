from pizza_store import PizzaStore
from simple_pizza_factory import SimplePizzaFactory


class PizzaTestDrive:

    def __init__(self):
        # instancing pizza factory and pizza store
        pizza_factory = SimplePizzaFactory()
        pizza_store = PizzaStore(pizza_factory)

        # ordering a pizza
        pizza = pizza_store.order_pizza("cheese")
        print(f"You ordered a {pizza.get_name()} \n")
