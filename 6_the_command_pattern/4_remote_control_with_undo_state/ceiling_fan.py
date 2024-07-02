class CeilingFan:
    # declaring static class variables
    HIGH: int = 3
    MEDIUM: int = 2
    LOW: int = 1
    OFF: int = 0

    def __init__(self, location: str):
        self.location = location
        self.speed = CeilingFan.OFF

    def high(self):
        self.speed = CeilingFan.HIGH

    def medium(self):
        self.speed = CeilingFan.MEDIUM

    def low(self):
        self.speed = CeilingFan.LOW

    def off(self):
        self.speed = CeilingFan.OFF

    def get_speed(self) -> int:
        return self.speed
