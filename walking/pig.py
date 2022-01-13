"""This module is for defining our "Pig" class"""

from datetime import date


class Pig:
    """Responsible for creating a pig object
    """

    def __init__(self, name, shift, food, chip_num) -> None:
        self.name = name
        self.species = "pig"
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
        self.food = food
        self.__chip_number = chip_num

    @property
    def chip_num(self):
        return self.__chip_number

    @chip_num.setter
    def chip_num(self, number):
        pass

    # @chip_num.setter
    # def chip_num(self, number):
    #     if isinstance(number, int):
    #         self.__chip_number = number
    #     else:
    #         raise TypeError(
    #             'Please provide a floating point value for the price')

    def feed(self):
        """prints a message about which animal was fed at what time
        """
        time_fed = date.today().strftime("%c")
        print(f"{self.name} the {self.species} was fed {self.food} on {time_fed}")

    def __str__(self) -> str:
        return f"{self.name} the {self.species}"
