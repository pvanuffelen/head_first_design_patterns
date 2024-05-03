from abc import ABC, abstractmethod
from pizza import Pizza


class PizzaStore(ABC):

    def order_pizza(self, type_: str):
        pizza = self.create_pizza(type_)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza

    @abstractmethod
    def create_pizza(self, type_: str):
        pass
