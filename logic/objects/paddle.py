import pygame

class Paddle():

  def __init__(self, game):
    game.objects.insert(0, self)
    self.game = game

    self.color = (255, 255, 255)
    self.rect = pygame.Rect((225, 315), (50, 10))
    self.surface = pygame.Surface((self.rect.width, self.rect.height))
    self.surface.fill(self.color)

  speed = 4

  def move(self, direction):
    ballHit = False
    if hasattr(self.game, 'ball'):
      ballHit = self.rect.colliderect(self.game.ball)
    
    if direction < 0 and self.rect.left >= 0 and not ballHit:
      self.rect.move_ip([self.speed * direction, 0])
    if direction > 0 and self.rect.right <= self.game.screenSize[0] and not ballHit:
      self.rect.move_ip([self.speed * direction, 0])

  # we will later use this to alter the ball's angle of movement
  def hit(self):
    # get distance from paddle center
    ballCenter = self.game.ball.rect.centerx
    paddleCenter = self.rect.centerx

    difference = ballCenter - paddleCenter

    # calculate change
    scaledDiff = difference / 40

    newDirection = scaledDiff, abs(scaledDiff) - 1

    # set new direction
    self.game.ball.changeDirection(newDirection)
