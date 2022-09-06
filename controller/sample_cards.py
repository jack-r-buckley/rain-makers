from card import Card
from enum import Enum

class Types(Enum):
  EARTH = "Earth"
  FIRE = "Fire"
  WATER = "Water"
  AIR = "Air"





mud_drake = Card("Mud Drake", Types.EARTH, 5, 30)
common_loon = Card("Common Loon", Types.AIR, 5, 25)
rabid_mole = Card("Rabid Mole", Types.EARTH, 2, 40)
horned_carp = Card("Horned Carp", Types.WATER, 9, 30)
steel_sparrow = Card("Steel Sparrow", Types.AIR, 10, 50)
seahorse_captain = Card("Seahorse Captain", Types.WATER, 3, 60)
fairy_cowboy = Card("Fairy Cowboy", Types.AIR, 7, 42)
combustion_snake = Card("Combustion Snake", Types.FIRE, 3, 14)
lava_slug = Card("Lava Slug", Types.FIRE, 16, 18)
radiation_worm = Card("Radiation Worm", Types.FIRE, 10, 30)

