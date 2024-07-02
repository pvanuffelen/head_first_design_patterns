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
        print(f"{self.location} ceiling fan is on high")

    def medium(self):
        self.speed = CeilingFan.MEDIUM
        print(f"{self.location} ceiling fan is on medium")

    def low(self):
        self.speed = CeilingFan.LOW
        print(f"{self.location} ceiling fan is on low")

    def off(self):
        self.speed = CeilingFan.OFF
        print(f"{self.location} ceiling fan is off")

    def get_speed(self) -> int:
        return self.speed
