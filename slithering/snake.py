"""This module is define our "Snake" class"""

from datetime import date


class Snake:
    """Responsible for creating a snake object
    """

    def __init__(self, name) -> None:
        self.name = name
        self.species = ""
        self.date_added = date.today()
        self.slithering = True
