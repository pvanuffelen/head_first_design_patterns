from abc import ABC


class Command(ABC):
    """The Command Interface"""
    def execute(self):
        raise NotImplementedError

    def undo(self):
        raise NotImplementedError
