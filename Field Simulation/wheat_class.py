from Crop import *

class Wheat(Crop):
    """A Wheat crop"""
    def __init__(self):
        super().__init__(1,3,6)
        self._type = "Wheat"
