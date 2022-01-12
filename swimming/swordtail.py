"""This module is define our "Swordtail" class"""

from datetime import date


class Swordtail:
    """Responsible for creating a swordtail object
    """

    def __init__(self, name) -> None:
        self.name = name
        self.species = ""
        self.date_added = date.today()
        self.swimming = True
