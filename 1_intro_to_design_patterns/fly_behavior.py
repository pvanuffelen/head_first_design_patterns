from abc import ABCMeta, abstractmethod


class FlyBehavior(metaclass=ABCMeta):
    """Class that mimics the interface that all flying behavior classes implement"""
    @abstractmethod
    def fly(self):
        """Fly method to be overridden by subclass"""
        raise NotImplementedError


class FlyWithWings(FlyBehavior):
    """Flying behavior implementation for ducks that DO fly"""
    def fly(self):
        print("I'm flying")


class FlyNoWay(FlyBehavior):
    """Flying behavior implementation for ducks that do NOT fly"""
    def fly(self):
        print("I can't fly")


class FlyRocketPowered(FlyBehavior):
    """Flying behavior implementation for ducks that do ROCKET POWERED"""
    def fly(self):
        print("I'm flying with a rocket!")
