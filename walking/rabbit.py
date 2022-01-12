"""This module is define our "Rabbit" class"""

from datetime import date

class Rabbit:
    """Responsible for creating a rabbit object
    """

    def __init__(self, name) -> None:
        self.name = name
        self.species = ""
        self.date_added = date.today()
        self.walking = True
