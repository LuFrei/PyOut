import pygame
from logic.game import *

class Renderer():

  pygame.font.init()
  hudFont = pygame.font.SysFont("gadugi", 18, True)


  scoreHud = hudFont.render(('Score: %d' % game.score), True, (255, 255, 255))
  livesHud = hudFont.render(('Lives: %d' % game.lives), True, (255, 255, 255))
  levelHud = hudFont.render(('Level %d' % game.level), True, (255, 255, 255))
  instructions = hudFont.render("Press SPACE to start playing", True, (255, 255, 255))

  titleFont = pygame.font.SysFont("gadugi", 64, True)
  title = titleFont.render('PyOut!', True, (255, 255, 255))

  gOFont = pygame.font.SysFont("gadugi", 42, True)
  gameOverHud = gOFont.render(('GAME OVER'), True, (255, 255, 255))


  def __init__(self, game):
    self.objects = game.objects
    self.screen = game.screen

  
  def updateHud(self):
    self.scoreHud = self.hudFont.render(('Score: %d' % game.score), True, (255, 255, 255))
    self.livesHud = self.hudFont.render(('Lives: %d' % game.lives), True, (255, 255, 255))
    self.levelHud = self.hudFont.render(('Level %d' % game.level), True, (255, 255, 255))

  

  def renderScreen(self):
    self.screen.fill((0, 0, 0))

    for object in self.objects:
      self.screen.blit(object.surface, object.rect)

    self.updateHud()
   

    self.screen.blit(self.scoreHud, (1, 1))
    self.screen.blit(self.livesHud, (430, 1))
    self.screen.blit(self.levelHud, (220, 1))

    if game.status != "playing":
      self.screen.blit(self.instructions, (135, 230))
      if game.status == "gameover":
        self.screen.blit(self.gameOverHud, (130, 150))
      elif game.status == "starting":
        self.screen.blit(self.title, (150, 100))

    pygame.display.flip()
    
