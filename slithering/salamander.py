"""This module is define our "Salamander" class"""

from datetime import date


class Salamander:
    """Responsible for creating a salamander object
    """

    def __init__(self, name) -> None:
        self.name = name
        self.species = ""
        self.date_added = date.today()
        self.slithering = True
