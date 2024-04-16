from beverage import Beverage


class Espresso(Beverage):

    def __init__(self):
        self.description: str = "Espresso"

    def cost(self) -> float:
        return 1.99
