from abc import ABCMeta, abstractmethod


class Subject(metaclass=ABCMeta):
    """Class to act as a subject interface"""
    @abstractmethod
    def register_observer(self, observer):
        """Method called to register an observer, takes an observer as an argument"""
        raise NotImplementedError

    @abstractmethod
    def remove_observer(self, observer):
        """Method called to remove an observer, takes an observer as an argument"""
        raise NotImplementedError

    @abstractmethod
    def notify_observers(self):
        """Method called to notify all observers when the Subject's state has changed"""
        raise NotImplementedError
