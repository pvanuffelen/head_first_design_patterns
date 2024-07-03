class TV:
    """Minimal TV class"""
    def __init__(self, location: str):
        self.location = location

    def on(self):
        print(f"{self.location} TV is on")

    def off(self):
        print(f"{self.location} TV is off")

    def set_dvd(self):
        print(f"{self.location} TV channel is set for DVD")
