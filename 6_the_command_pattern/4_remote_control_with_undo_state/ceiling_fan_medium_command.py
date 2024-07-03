from command import Command
from ceiling_fan import CeilingFan


class CeilingFanMediumCommand(Command):
    def __init__(self, ceiling_fan: CeilingFan):
        self.ceiling_fan = ceiling_fan
        self.prev_speed: int = self.ceiling_fan.get_speed()

    def execute(self):
        self.prev_speed = self.ceiling_fan.get_speed()
        self.ceiling_fan.medium()

    def undo(self):
        match self.prev_speed:
            case CeilingFan.HIGH:
                self.ceiling_fan.high()
            case CeilingFan.MEDIUM:
                self.ceiling_fan.medium()
            case CeilingFan.LOW:
                self.ceiling_fan.low()
            case CeilingFan.OFF:
                self.ceiling_fan.off()
