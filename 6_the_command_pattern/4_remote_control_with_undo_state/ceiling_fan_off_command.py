from command import Command
from ceiling_fan import CeilingFan


class CeilingFanOffCommand(Command):
    def __init__(self, ceiling_fan: CeilingFan):
        self.ceiling_fan = ceiling_fan
        self.prev_speed: int = self.ceiling_fan.get_speed()

    def execute(self):
        self.prev_speed = self.ceiling_fan.get_speed()
        self.ceiling_fan.off()

    def undo(self):
        if self.prev_speed == CeilingFan.HIGH:
            self.ceiling_fan.high()
        elif self.prev_speed == CeilingFan.MEDIUM:
            self.ceiling_fan.medium()
        elif self.prev_speed == CeilingFan.LOW:
            self.ceiling_fan.low()
        elif self.prev_speed == CeilingFan.OFF:
            self.ceiling_fan.off()
