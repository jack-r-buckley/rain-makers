from card import Card
from enum import Enum

class Types(Enum):
  EARTH = "Earth"
  FIRE = "Fire"
  WATER = "Water"
  AIR = "Air"




cards={
'antipigeon': Card("AntiPigeon", Types.AIR, 0, 85),
'windy_whippet': Card("Windy Whippet", Types.EARTH, 9, 21),
'gregarian_molepod': Card("Gregarian Molepod", Types.WATER, 9, 30),
'cockpit_cobra': Card("Cockpit Cobra", Types.AIR, 10, 50),
'grimsby': Card("Grimsby", Types.WATER, 3, 60),
'lard_wallet': Card("Lard Wallet", Types.AIR, 7, 42),
'pesky_tuna': Card("Pesky Tuna", Types.FIRE, 3, 14),
'graveyard_tom': Card("Graveyard Tom", Types.FIRE, 16, 18),
'umc_mech': Card("UMC Mech", Types.EARTH, 5, 30),
'rocksta': Card("Rocksta", Types.EARTH, 6, 30),
'ribeyed_flagon': Card("Ribeyed Flagon", Types.EARTH, 6, 55),
'raspy_wombo': Card("Raspy Wombo", Types.AIR, 1, 25),
'bigeye_banana': Card("Bigeye Banana", Types.EARTH, 6, 40),
'pickle_poncho': Card("Pickle Poncho", Types.WATER, 1, 50),
'growfast': Card("GrowFast", Types.AIR, 6, 34),
'brilliam_willsby': Card("Brilliam Willsby", Types.WATER, 6, 55),
'rudy_gobert': Card("Rudy Gobert", Types.AIR, 7, 42),
'carpet_mike': Card("Carpet Mike", Types.FIRE, 2, 16),
'ariza_van_welson': Card("ArizaVanWelson", Types.FIRE, 8, 38),
'camp_fortuna': Card("CAMP Fortuna", Types.FIRE, 0, 30),
}
