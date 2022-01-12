"""This module is define our "MiniHorse" class"""

from datetime import date


class MiniHorse:
    """Responsible for creating a mini-horse object
    """

    def __init__(self, name) -> None:
        self.name = name
        self.species = ""
        self.date_added = date.today()
        self.walking = True