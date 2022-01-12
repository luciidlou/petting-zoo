"""This module is define our "Guppy" class"""

from datetime import date


class Guppy:
    """Responsible for creating a guppy object
    """

    def __init__(self, name) -> None:
        self.name = name
        self.species = ""
        self.date_added = date.today()
        self.swimming = True
