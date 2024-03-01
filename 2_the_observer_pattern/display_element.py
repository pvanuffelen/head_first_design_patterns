from abc import ABCMeta, abstractmethod


class DisplayElement(metaclass=ABCMeta):
    """Class to act as an interface. Contains just one method, display()"""

    @abstractmethod
    def display(self):
        raise NotImplementedError
