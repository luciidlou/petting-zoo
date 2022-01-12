"""This module is define our "Llama" class"""

from datetime import date


class Llama:
    """Responsible for creating a llama object
    """

    def __init__(self, name, shift, food) -> None:
        self.name = name
        self.species = "llama"
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
        self.food = food

    def feed(self):
        """prints a message about which animal was fed at what time
        """
        time_fed = date.today().strftime("%c")
        print(f"{self.name} the {self.species} was fed {self.food} on {time_fed}")

    def __str__(self) -> str:
        return f"{self.name} the {self.species}"
