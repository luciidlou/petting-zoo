"""This module is define our "Bristlenose" class"""

from datetime import date

class Bristlenose:
    """Responsible for creating a bristlenose object
    """

    def __init__(self, name) -> None:
        self.name = name
        self.species = ""
        self.date_added = date.today()
        self.swimming = True
        