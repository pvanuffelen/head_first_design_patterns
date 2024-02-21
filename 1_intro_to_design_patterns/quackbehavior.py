from abc import ABCMeta, abstractmethod

class QuackBehavior(metaclass=ABCMeta):
    """Class that mimics the quack behavior interface"""
    @abstractmethod
    def quack(self):
        raise NotImplementedError

class Quack(QuackBehavior):

    def quack(self):
        print("Quack")

class MuteQuack(QuackBehavior):

    def quack(self):
        print("<< Silence >>")

class Squeak(QuackBehavior):

    def quack(self):
        print("Squeak")
