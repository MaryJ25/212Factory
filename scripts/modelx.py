from main import Tesla


class ModelX(Tesla):
    """Creates the ModelX subclass of Tesla. Model is set to X, colour needs to be given when called."""

    def __init__(self, color: str, autopilot: bool = False):
        super().__init__("X", color, autopilot, 0.125)

    def open_doors(self):
        return "Doors open towards the roof"
