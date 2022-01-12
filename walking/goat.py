"""This module is define our "Goat" class"""

from datetime import date


class Goat:
    """Responsible for creating a goat object
    """

    def __init__(self, name) -> None:
        self.name = name
        self.species = ""
        self.date_added = date.today()
        self.walking = True
