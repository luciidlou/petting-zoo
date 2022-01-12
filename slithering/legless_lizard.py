"""This module is define our "LeglessLizard" class"""

from datetime import date


class LeglessLizard:
    """Responsible for creating a legless lizard object
    """

    def __init__(self, name) -> None:
        self.name = name
        self.species = ""
        self.date_added = date.today()
        self.slithering = True
