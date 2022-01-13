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

    @property
    def last_critter_added(self):
        """This function gives us the last animal in the animal list

        Returns:
            dictionary: last index in the animal list
        """
        most_recent_animal = self.animals[-1]
        return most_recent_animal


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

    @property
    def last_critter_added(self):
        """This function gives us the last animal in the animal list

        Returns:
            dictionary: last index in the animal list
        """
        most_recent_animal = self.animals[-1]
        return most_recent_animal


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

    @property
    def last_critter_added(self):
        """This function gives us the last animal in the animal list

        Returns:
            dictionary: last index in the animal list
        """
        most_recent_animal = self.animals[-1]
        return most_recent_animal
