class Card:
  def __init__(self, name, type, pwr, hp):
    self.name = name
    self.pwr = pwr
    self.type = type
    self.hp = hp

  def deal_damage(self):
    return self.pwr

  def take_damage(self, damage):
    self.hp -= damage
    if self.hp <0: self.hp = 0

