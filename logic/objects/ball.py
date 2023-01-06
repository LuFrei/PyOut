import pygame

class Ball():

  def __init__(self, game, speed = 5.5):
    game.objects.append(self)
    self.game = game

    self.color = (255, 255, 255)
    self.rect = pygame.Rect((243, 300), (15, 15))
    self.surface = pygame.Surface((self.rect.width, self.rect.height))
    self.surface.fill(self.color)
    
    self.direction = [2, 2]
    self.speed = speed



  def changeDirection(self, newDirection):
    for i in range(2):
      self.direction[i] = newDirection[i] * self.speed

 


  def checkCollision(self):
    # screen border
    if (self.rect.left < 0 and self.direction[0] < 0) or (self.rect.right > self.game.screenSize[0] and self.direction[0] > 0):
        self.bounce('x')
    if self.rect.top < 0:
        self.bounce('y')
    elif self.rect.bottom > self.game.screenSize[1]:
        self.game.loseLife()
        self.resetBall()

    # other objects
    hitIdx = self.rect.collidelist(self.game.objects)

    if hitIdx >= 0 and hitIdx != len(self.game.objects) - 1:
      hit = self.game.objects[hitIdx]

      if(hit == self.game.paddle) and self.direction[1] < 0:
        return
      

      hitCorner = ()
      ballCorner = ()

      # get hit corner
      if self.direction[0] > 0 and self.direction[1] < 0: #"NE"
        ballCorner = self.rect.topright
        hitCorner = hit.rect.bottomleft
      elif self.direction[0] > 0 and self.direction[1] > 0: #"SE"
        ballCorner = self.rect.bottomright
        hitCorner = hit.rect.topleft
      elif self.direction[0] <= 0 and self.direction[1] > 0: #"SW"
        ballCorner = self.rect.bottomleft
        hitCorner = hit.rect.topright
      elif self.direction[0] <= 0 and self.direction[1] < 0: #"NW"
        ballCorner = self.rect.topleft
        hitCorner = hit.rect.bottomright  
      

      # check what axis to bounce
      disparity = (ballCorner[0] - hitCorner[0], ballCorner[1] - hitCorner[1])
      if abs(disparity[0]) > abs(disparity[1]):
        self.bounce('y')
      else:
        self.bounce('x')

      
      # notify object we hit that we hit them
      hit.hit()

      

  def bounce(self, axis):
      if axis == "y":
        self.direction[1] = -self.direction[1]
      elif axis == "x":
        self.direction[0] = -self.direction[0]
      else:
        print("Error calling bounce: please specificy what axis to deflect: 'x' or 'y'")


    
  def move(self):
    self.rect.move_ip(self.direction)
    self.checkCollision()

  def resetBall(self):
    self.rect.x = 140
    self.rect.y = 300
    self.direction = [2,-2]