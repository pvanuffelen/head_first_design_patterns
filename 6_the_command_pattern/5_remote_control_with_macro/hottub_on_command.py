from command import Command
from hottub import Hottub


class HottubOnCommand(Command):
    """Class that implements the Command interface"""
    def __init__(self, hottub):
        self.hottub: Hottub = hottub

    def execute(self):
        self.hottub.heating()
        self.hottub.bubbling()

    def undo(self):
        self.hottub.cooling()
