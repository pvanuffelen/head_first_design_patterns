from abc import abstractmethod
from fly_behavior import FlyBehavior
from quack_behavior import QuackBehavior


class Duck:
    """Duck class from which all other duck classes inherit from"""
    def __init__(self):
        self.fly_behavior = FlyBehavior()  # declare attribute to fly behavior 'interface'
        self.quack_behavior = QuackBehavior()  # declare attribute to quack behavior 'interface'

    @abstractmethod
    def display(self):
        """Abstract method to display duck (abstract=all subclasses must have display() method)"""
        pass

    def perform_fly(self):
        """Use the fly behavior interface to perform fly()"""
        self.fly_behavior.fly()

    def perform_quack(self):
        """Use the quack behavior interface to perform quack"""
        self.quack_behavior.quack()

    def swim(self):
        print("All ducks float, even decoys!")

    def set_fly_behavior(self, fly_behavior):
        """Setter method for the fly_behavior"""
        self.fly_behavior = fly_behavior

    def set_quack_behavior(self, quack_behavior):
        """Setter method for the quack_behavior"""
        self.quack_behavior = quack_behavior
