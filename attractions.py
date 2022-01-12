"""This module is where we define our classes for various attractions at the petting zoo"""


class PettingZoo:
    """Responsible for creating a petting zoo attraction object"""

    def __init__(self, attraction_name, description) -> None:
        self.attraction_name = attraction_name
        self.description = description
        self.animals = []

    def add_animal(self, animal):
        """responsible for appending an animal onto the animals list

        Args:
            animal (dictionary): the animal we want to append
        """
        self.animals.append(animal)


class SnakePit:
    """Responsible for creating a snake pit attraction object"""

    def __init__(self, attraction_name, description) -> None:
        self.attraction_name = attraction_name
        self.description = description
        self.animals = []

    def add_animal(self, animal):
        """responsible for appending an animal onto the animals list

        Args:
            animal (dictionary): the animal we want to append
        """
        self.animals.append(animal)


class Wetlands:
    """Responsible for creating a wetlands attraction object"""

    def __init__(self, attraction_name, description) -> None:
        self.attraction_name = attraction_name
        self.description = description
        self.animals = []

    def add_animal(self, animal):
        """responsible for appending an animal onto the animals list

        Args:
            animal (dictionary): the animal we want to append
        """
        self.animals.append(animal)
