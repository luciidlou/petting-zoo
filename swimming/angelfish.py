"""This module is define our "Angelfish" class"""

from datetime import date


class Angelfish:
    """Responsible for creating a angelfish object
    """

    def __init__(self, name) -> None:
        self.name = name
        self.species = ""
        self.date_added = date.today()
        self.swimming = True
