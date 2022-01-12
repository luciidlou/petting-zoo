"""This module is define our "Donkey" class"""

from datetime import date


class Donkey:
    """Responsible for creating a donkey object
    """

    def __init__(self, name) -> None:
        self.name = name
        self.species = ""
        self.date_added = date.today()
        self.walking = True
