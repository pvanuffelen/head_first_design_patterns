from pizza import Pizza


class SimplePizzaFactory:
    """Simple Pizza Factory class that has one job: Creating pizzas for clients"""

    def create_pizza(self, type_: str):
        """This part is pulled out of the 'order_pizza() method"""
        pizza = Pizza

        if type_=="cheese":
            pizza = CheesePizza
        elif type_=="pepperoni":
            pizza = PepperoniPizza
        elif type_=="clam":
            pizza = ClamPizza
        elif type_=="veggie":
            pizza = VeggiePizza

        return pizza
