import pygame

class Brick():

  color = (255, 255, 255)
  position = ()
  value = 100

  def __init__(self, game, position, color):
    game.objects.insert(1, self)
    
    self.position = position
    self.color = color
    self.game = game

    self.rect = pygame.Rect(position, (50, 15))
    self.surface = pygame.Surface((self.rect.width, self.rect.height))
    self.surface.fill(color)


  def hit(self):
    self.game.score += self.value
    myIdx = self.game.objects.index(self)
    del self.game.objects[myIdx]
    self.game.checkRemainingBricks()
    