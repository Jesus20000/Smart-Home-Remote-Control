class Light:
    def __init__(self, location="Generic"):
        self.location = location
        self.state = "off"

    def on(self):
        self.state = "on"
        print(f"{self.location} Light is ON")

    def off(self):
        self.state = "off"
        print(f"{self.location} Light is OFF")