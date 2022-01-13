"""This module is define our "Guppy" class"""

from datetime import date


class Guppy:
    """Responsible for creating a guppy object
    """

    def __init__(self, name, food) -> None:
        self.name = name
        self.species = "guppy"
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
    