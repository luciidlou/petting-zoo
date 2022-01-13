"""This module is where we make instances of all the different animal classes
"""

from walking import Donkey, Goat, Llama, MiniHorse, Pig, Rabbit
from slithering import Snake, Salamander, LeglessLizard
from swimming import Swordtail, Bristlenose, Rainbowfish, Angelfish, SiameseAlgaeEater, Guppy
from attractions import PettingZoo, Wetlands, SnakePit



# walking animals
george = Llama("George", "morning", "oats hay")
sam = Donkey("Sam", "midday", "carrots")
roger = MiniHorse("Roger", "afternoon", "carrots")
judith = Pig("Judith", "morning", "soybean meal", 3971134)
jack = Rabbit("Jack", "midday", "orchard grass")
michael = Goat("Michael", "afternoon", "chaff hay")

# slithering animals
sampson = Snake("Sampson", "mouse")
larry = LeglessLizard("Larry", "lizard grub")
susan = Salamander("Susan", "buffalo worms")

# swimming animals
zach = Swordtail("Zach", "fish food")
byron = Bristlenose("Byron", "fish food")
rick = Rainbowfish("Rick", "fish food")
angie = Angelfish("Angie", "fish food")
ethan = SiameseAlgaeEater("Ethan", "fish food")
guillermo = Guppy("Guillermo", "fish food")

# Create three different attractions (instances)
varmint_village = PettingZoo(
    "Varmint Village", "cute and fuzzy critters to cuddle")
critter_cove = Wetlands(
    "Critter Cove", "one-acre wetlands and wet bar with fantastic fish")
slither_inn = SnakePit(
    "The Slither Inn", "housing more snakes than an Indiana Jones movie")

# add animals to Varmint Village
varmint_village.add_animal(george)
varmint_village.add_animal(sam)
varmint_village.add_animal(roger)
varmint_village.add_animal(judith)
varmint_village.add_animal(jack)
varmint_village.add_animal(michael)

# add animals to Critter Cove
critter_cove.add_animal(zach)
critter_cove.add_animal(byron)
critter_cove.add_animal(rick)
critter_cove.add_animal(angie)
critter_cove.add_animal(ethan)
critter_cove.add_animal(guillermo)


# # add animals to The Slither Inn
# slither_inn.add_animal(sampson)
# slither_inn.add_animal(larry)
# slither_inn.add_animal(susan)

# # print information about Varmint Village and list its animals
# print(f"{varmint_village.attraction_name} is where you'll find {varmint_village.description}, like")
# for animal in varmint_village.animals:
#     print(animal)

# # print information about Critter Cove and list its animals
# print(f"{critter_cove.attraction_name} is where you'll find {critter_cove.description}, like")
# for animal in critter_cove.animals:
#     print(animal)

# # print information about The Slither Inn and list its animals
# print(f"{slither_inn.attraction_name} is where you'll find {slither_inn.description}, like")
# for animal in slither_inn.animals:
#     print(animal)

print("------------------------")

print(judith.chip_num)
judith.chip_num = 12
print(judith.chip_num)

print("------------------------")
print(
    f"The last animal added to {varmint_village.attraction_name} was {varmint_village.last_critter_added}")
