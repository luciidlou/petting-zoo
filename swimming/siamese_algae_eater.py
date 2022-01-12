"""This module is define our "SiameseAlgaeEater" class"""

from datetime import date


class SiameseAlgaeEater:
    """Responsible for creating a Siamese Algae Eater object
    """

    def __init__(self, name) -> None:
        self.name = name
        self.species = ""
        self.date_added = date.today()
        self.swimming = True
