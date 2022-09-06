import time
import sys
from sample_cards import *

class Player:
    def __init__(self, name):
      self.name = name
      self.hp = 50
      self.position = None

    def check_if_dead(self):
      print(f"{self.name}: {self.hp}")
      if self.hp <= 0:
        print(f"{self.name} lost!")
        sys.exit()

class Game_Session:

  class Slot:
    def __init__(self):
      self.card = None



  def __init__(self, player1, player2):
    self.player1 = player1
    self.player1.position = 0
    self.player2 = player2
    self.player2.position = 1
    self.PET_SLOTS = 5
    self.TOTAL_PLAYERS = 2

    self.field = [[self.Slot() for _ in range(self.PET_SLOTS)] for _ in range(self.TOTAL_PLAYERS)]

  def take_turn(self, player, opponent):

    for idx in range(len(self.field[player.position])):
      try:
        self.field[opponent.position][idx].card.take_damage(self.field[player.position][idx].card.deal_damage())
      except AttributeError: 
        try:
          opponent.hp -= (self.field[player.position][idx].card.deal_damage())
        except:
          pass


  def kill_card_if_dead(self, slot):
    try:
      if slot.card.hp <= 0: 
        return None
    except:
      pass
    return slot
    

  def check_dead_pets(self):
      self.field=[[self.kill_card_if_dead(slot) for slot in player] for player in self.field]
      for idx in range(self.PET_SLOTS):
        try:
          print(f"{self.field[0][idx].card.name}({self.field[0][idx].card.type}): {self.field[0][idx].card.hp} HP")
        except:
          print("empty...")
        try:
          print(f"{self.field[1][idx].card.name}({self.field[1][idx].card.type}): {self.field[1][idx].card.hp} HP")
        except:
          print("empty...")
        print("\n")

            

      

  def run_game(self, player1, player2):
    self.take_turn(player1, player2)
    self.check_dead_pets()
    self.player1.check_if_dead()
    self.player2.check_if_dead()
    self.take_turn(player2, player1)
    self.check_dead_pets()
    self.player1.check_if_dead()
    self.player2.check_if_dead()
    time.sleep(1)
    self.run_game(player1, player2)


if __name__ == "__main__":
  p1 = Player("Keri")
  p2 = Player("Tama")
  game = Game_Session(p1, p2)
  game.field[0][0].card = mud_drake
  game.field[0][1].card = rabid_mole
  game.field[0][2].card = steel_sparrow
  game.field[0][3].card = seahorse_captain
  game.field[0][4].card = combustion_snake
  game.field[1][0].card = common_loon
  game.field[1][1].card = horned_carp
  game.field[1][2].card = fairy_cowboy
  game.field[1][3].card = lava_slug
  game.field[1][4].card = radiation_worm
  game.run_game(p1, p2)


