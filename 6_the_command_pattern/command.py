from abc import ABC, abstractmethod


class Command(ABC):
    """The Command Interface"""

    def execute(self):
        raise NotImplementedError
