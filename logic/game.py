import pygame
from pygame.locals import *

from logic.objects.brick import *
from logic.objects.ball import *
from logic.objects.paddle import *


class Game():

  # events
  GAMEOVER = []
  GAMESTART = []

  score = 0
  lives = 5
  level = 1

  status = "starting"

  objects = []

  screenSize = (500, 350)

  screen = pygame.display.set_mode(screenSize)

  def __init__(self):
    pass

  def gameStart(self):
    self.ball = Ball(self)
    self.paddle = Paddle(self)
    self.createGrid()
    self.status = "starting"
    self.lives = 5
    self.score = 0
    self.level = 1

  def createGrid(self, rows = 8, columns = 8):
    xSpacing = 55
    ySpacing = 20

    colors = [
      (0, 0, 255), 
      (200, 0, 200), 
      (255, 0, 0), 
      (255, 150, 0), 
      (255, 255, 0), 
      (0, 255, 0),
      (0, 255, 255), 
      (255, 255, 255)
    ]

    for i in range(rows):
      y = ySpacing * i + (30)

      for j in range(columns):
        x = xSpacing * j + (30)
        Brick(self, (x, y), colors[i])

  # A way to tell the game to initialize the next level
  def nextLevel(self):
    self.level += 1

    # make sure everything from last ellve is cleared
      # delete stuff
    del self.ball
    del self.paddle
    for x in range(len(self.objects)):
        del self.objects[0]

    # reinstantiate stuff
    self.ball = Ball(self)
    self.ball.speed += 0.5 * self.level
    self.paddle = Paddle(self)

    # create a new grid
    self.createGrid()
    # keep score and lives
    # make new ball (with greater speed)
    

    # check when all bricks are gone
  def checkRemainingBricks(self):
    remainingBricks = len(self.objects) - 2

    if remainingBricks <= 0:
      self.nextLevel()
    


  def play(self):
    keys = pygame.key.get_pressed()

    if self.status == "playing":

      if keys[K_LEFT]:
        self.paddle.move(-1)
      if keys[K_RIGHT]:
        self.paddle.move(1)
      
      self.ball.move()  
    else:
      if keys[K_SPACE]:
        self.gameStart()
        self.status = "playing"


  def loseLife(self):
    self.lives -= 1
    if self.lives <= 0:
      # game over
      del self.ball
      del self.paddle
      for x in range(len(self.objects)):
        del self.objects[0]
      # print("objects: ", self.objects, "\nball: ", self.ball, "\npaddle: ", self.paddle)
      self.broadcast("GAMEOVER")
      self.status = "gameover"
      pass




  def subscribeTo(self, event, func):
    process = []
    if event == "GAMEOVER":
      process = self.GAMEOVER
    elif event == "GAMESTART":
      process = self.GAMESTART
    else:
      print("invalid event given!")
      return

    process.append(func)
    return lambda: self.unsubscribe(process, func)


  def unsubscribe(self, event, func):
    evtIdx = event.index(func)
    del event[evtIdx]


  def broadcast(self, event):
    process = []
    if event == "GAMEOVER":
      process = self.GAMEOVER
    elif event == "GAMESTART":
      process = self.GAMESTART
    else:
      print("invalid event given!")
      return
    
    for func in process:
      func()



game = Game()

