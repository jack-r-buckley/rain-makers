import os
import pygame
import assets  as a

os.environ["SDL_VIDEODRIVER"]=a.Game_Settings.SDL_VIDEODRIVER.value

pygame.display.init()
window = pygame.display.set_mode(
  (a.Game_Settings.WIDTH.value, a.Game_Settings.HEIGHT.value))
pygame.display.set_caption("Rain Makers 0.01")

clientNumber = 0

class Player():
  def __init__(self, x, y, width, height, colour, speed):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.colour = colour
    self.speed = speed
    self.rect = (x, y, width, height)

  def draw(self, window):
    pygame.draw.rect(window, self.colour, self.rect)

  def move(self):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and self.x > 0:
      self.x -= self.speed 
    if keys[pygame.K_d]:
    # and self.x + self.width > a.Game_Settings.WIDTH.value:
      self.x  += self.speed 
    if keys[pygame.K_w] and self.y > 0:
      self.y  -= self.speed 
    if keys[pygame.K_s]:
      #  and self.y + self.height > a.Game_Settings.HEIGHT.value:
      self.y  += self.speed 
    self.rect=(self.x, self.y, self.width, self.height)
    

def redrawWindow(window, player):
  window.fill(a.Colours.WHITE.value)
  player.draw(window)
  pygame.display.update()


def main():
  clock = pygame.time.Clock()
  run = True
  p = Player(250, 250, 30, 30, a.Colours.PURPLE.value, 3)
  while run:
    clock.tick(a.Game_Settings.FPS.value)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
        pygame.quit()
    redrawWindow(window, p)
    p.move()


if __name__ == '__main__':
  main()
  # p = Player(250, 250, 30, 30, a.Colours.PURPLE.value, 3)
  # print(
  #   p.speed, p.x,p.y
  # )
