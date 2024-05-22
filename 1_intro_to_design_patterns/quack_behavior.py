from abc import ABCMeta, abstractmethod


class QuackBehavior(metaclass=ABCMeta):
    """Class that mimics the quack behavior interface"""

    @abstractmethod
    def quack(self):
        raise NotImplementedError


class Quack(QuackBehavior):
    """Quack behavior implementation for ducks that DO quack"""

    def quack(self):
        print("Quack")


class MuteQuack(QuackBehavior):
    """ "Quack behavior implementation for ducks that do NOT make a sound"""

    def quack(self):
        print("<< Silence >>")


class Squeak(QuackBehavior):
    """Quack behavior implementation for ducks that SQUEAK"""

    def quack(self):
        print("Squeak")
