import os, sys
import pygame

from logic.game import *
from render.renderer import *


if not pygame.font: print('Warning, fonts disabled')
if not pygame.mixer: print('Warning, sound disabled')

clock = pygame.time.Clock()

renderer = Renderer(game)

# game loop
while 1:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: sys.exit()

  clock.tick(60)

  game.play()
  
  renderer.renderScreen()