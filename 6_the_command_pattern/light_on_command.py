from command import Command
from light import Light


class LightOnCommand(Command):
    """"""
    def __init__(self, light):
        self.light: Light = light

    def execute(self):
        self.light.on()
