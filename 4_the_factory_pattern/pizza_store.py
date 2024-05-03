from abc import ABC, abstractmethod
from pizza import Pizza


class PizzaStore(ABC):

    def order_pizza(self, type: str):

        pizza = create_pizza(type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza

    @abstractmethod
    def create_pizza(self):
        pass
