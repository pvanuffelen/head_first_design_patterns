from pizza import Pizza
from ingredients import Dough, Sauce, Cheese

class CheesePizza(Pizza):

    def __init__(self):
        super().__init__()
        self.dough = Dough()
        self.sauce = Sauce()
        self.toppings = "cheese"
        self.set_name("Cheese Pizza")
