from animal_class import *

class Cow(animal):
    """A Cow Animal"""
    def __init__(self):
        super().__init__(1,10,12)
        self._type = "Cows"
