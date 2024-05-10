from pizza import Pizza


class ChicagoStyleCheesePizza(Pizza):

    def __init__(self):
        super().__init__()
        self.name = "Chicago Style Deep Dish Cheese Pizza"
        self.dough = "Extra Thick Crust Dough"
        self.sauce = "Plum Tomato Sauce"

        self.toppings.append("Shredded Mozzarella Cheese")

    @staticmethod
    def cut():
        print("Cutting the pizza into square slices")
