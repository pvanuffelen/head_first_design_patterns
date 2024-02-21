from abc import abstractmethod, ABC


class Duck(ABC):

    def __init__(self):
        self.fly_behavior = FlyBehavior()
        self.quack_behavior = QuackBehavior()

    @abstractmethod
    def display(self):
        pass

    def perform_fly(self):
        self.fly_behavior.fly()

    def perform_quack(self):
        self.quack_behavior.quack()

    def swim(self):
        print("All ducks float, even decoys!")
