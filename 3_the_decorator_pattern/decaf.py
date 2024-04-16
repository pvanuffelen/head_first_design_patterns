from beverage import Beverage


class Decaf(Beverage):

    def __init__(self):
        self.description: str = "Decaf Coffee"

    def cost(self) -> float:
        return 1.05
