from beverage import Beverage


class DarkRoast(Beverage):

    def __init__(self):
        self.description: str = "Dark Roast Coffee"

    def cost(self) -> float:
        return 0.99
