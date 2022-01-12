"""This module is define our "SiameseAlgaeEater" class"""

from datetime import date


class SiameseAlgaeEater:
    """Responsible for creating a Siamese Algae Eater object
    """

    def __init__(self, name, food) -> None:
        self.name = name
        self.species = "siamese-algae-fish"
        self.date_added = date.today()
        self.swimming = True
        self.food = food

    def feed(self):
        """prints a message about which animal was fed at what time
        """
        time_fed = date.today().strftime("%c")
        print(f"{self.name} the {self.species} was fed {self.food} on {time_fed}")

    def __str__(self) -> str:
        return f"{self.name} the {self.species}"
    