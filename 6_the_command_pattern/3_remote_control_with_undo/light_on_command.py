from command import Command
from light import Light


class LightOnCommand(Command):
    """Class that implements the Command interface"""
    def __init__(self, light):
        self.light: Light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()
