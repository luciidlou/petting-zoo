"""This module is define our "Llama" class"""

from datetime import date

class Llama:
    """Responsible for creating a llama object
    """

    def __init__(self, name) -> None:
        self.name = name
        self.species = "llama"
        self.date_added = date.today()
        self.walking = True
