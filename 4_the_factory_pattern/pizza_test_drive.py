from ny_pizza_store import NYStylePizzaStore
from chicago_pizza_store import ChicagoStylePizzaStore


class PizzaTestDrive:

    def __init__(self):
        # instancing the pizza stores
        ny_store = NYStylePizzaStore()
        # chicago_store = ChicagoStylePizzaStore()

        # ordering Ethan's pizza
        pizza = ny_store.order_pizza("cheese")
        print(f"Ethan ordered a {pizza.get_name()} \n")

        # ordering Joel's pizza
        # pizza = chicago_store.order_pizza("cheese")
        # print(f"Joel ordered a {pizza.get_name()} \n")
