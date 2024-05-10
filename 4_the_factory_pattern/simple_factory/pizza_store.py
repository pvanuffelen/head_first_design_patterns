from simple_pizza_factory import SimplePizzaFactory


class PizzaStore:

    def __init__(self, factory: SimplePizzaFactory):
        self.factory = factory

    def order_pizza(self, type_):
        """Method that uses the factory to create its pizzas. No more concrete instantiations here!"""
        pizza = self.factory.create_pizza(type_)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza

    # other methods here
