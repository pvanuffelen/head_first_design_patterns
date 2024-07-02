class Light:
    def __init__(self, room: str = "default"):
        self.room = room

    def on(self):
        print(f"{self.room} light on")

    def off(self):
        print(f"{self.room} light off")
