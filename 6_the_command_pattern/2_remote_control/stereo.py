class Stereo:
    """Minimal stereo class"""
    def __init__(self, room: str):
        self.room = room

    def on(self):
        print(f"{self.room} stereo is on")

    def off(self):
        print(f"{self.room} stereo is off")

    def set_cd(self):
        print(f"{self.room} stereo is set for CD input")

    def set_volume(self, volume: int):
        print(f"{self.room} stereo volume is set {volume}")
