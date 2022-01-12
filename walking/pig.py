"""This module is define our "Pig" class"""

from datetime import date

class Pig:
    """Responsible for creating a pig object
    """

    def __init__(self, name) -> None:
        self.name = name
        self.species = ""
        self.date_added = date.today()
        self.walking = True
