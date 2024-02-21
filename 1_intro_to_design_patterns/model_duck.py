from duck import Duck
from fly_behavior import FlyNoWay
from quack_behavior import Quack

class ModelDuck(Duck):
    """Model duck class that begins life without a way to fly"""

    def __init__(self):
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = Quack()

    def display(self):
        print("I'm a model duck")
