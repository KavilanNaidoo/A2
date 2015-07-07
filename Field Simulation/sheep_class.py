from animal_class import *

class Sheep(animal):
    """A Sheep Animal"""
    def __init__(self):
        super().__init__(1,5,9)
        self._type = "Sheep"
