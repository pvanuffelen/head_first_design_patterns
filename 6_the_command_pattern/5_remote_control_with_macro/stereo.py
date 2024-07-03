class Stereo:
    """Minimal stereo class"""
    def __init__(self, location: str):
        self.location = location

    def on(self):
        print(f"{self.location} stereo is on")

    def off(self):
        print(f"{self.location} stereo is off")

    def set_cd(self):
        print(f"{self.location} stereo is set for CD input")

    def set_volume(self, volume: int):
        print(f"{self.location} stereo volume is set {volume}")
