"""This module is define our "Rainbowfish" class"""

from datetime import date


class Rainbowfish:
    """Responsible for creating a rainbowfish object
    """

    def __init__(self, name) -> None:
        self.name = name
        self.species = ""
        self.date_added = date.today()
        self.swimming = True
