from duck import Duck
from quack_behavior import Quack
from fly_behavior import FlyWithWings


class MallardDuck(Duck):

    def __init__(self):
        self.quack_behavior = Quack()
        self.fly_behavior = FlyWithWings()

    def display(self):
        print("I'm a real Mallard duck")
