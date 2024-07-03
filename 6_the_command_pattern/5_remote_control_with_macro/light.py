class Light:
    def __init__(self, location: str = "default"):
        self.location = location

    def on(self):
        print(f"{self.location} light on")

    def off(self):
        print(f"{self.location} light off")
