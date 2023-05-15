import pygame as pg
from pygame.sprite import Sprite
from settings import *
from random import randint

vec = pg.math.Vector2

# classes

# Player class
class Paddle:
      
    # Take the initial position,
    # dimensions, speed and color of the object
    def __init__(self, posx, posy, width, height, speed, color):
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
        # Rect that is used to control the
        # position and collision of the object
        self.playerRect = pg.Rect(posx, posy, width, height)
        # Object that is blit on the screen
        self.player = pg.draw.rect(screen, self.color, self.playerRect)
  
    # Used to display the object on the screen
    def display(self):
        self.player = pg.draw.rect(screen, self.color, self.playerRect)
  
    # Used to update the state of the object
    # yFac represents the direction of the striker movement
    # if yFac == -1 ==> The object is moving upwards
    # if yFac == 1 ==> The object is moving downwards
    # if yFac == 0 ==> The object is not moving
    def update(self, yFac):
        self.posy = self.posy + self.speed*yFac
  
        # Restricting the striker to be below
        # the top surface of the screen
        if self.posy <= 0:
            self.posy = 0
        # Restricting the striker to be above
        # the bottom surface of the screen
        elif self.posy + self.height >= HEIGHT:
            self.posy = HEIGHT-self.height
  
        # Updating the rect with the new values
        self.playerRect = (self.posx, self.posy, self.width, self.height)
  
    # Used to render the score on to the screen
    # First, create a text object using the font.render() method
    # Then, get the rect of that text using the get_rect() method
    # Finally blit the text on to the screen
    def displayScore(self, text, score, x, y, color):
        text = font20.render(text+str(score), True, color)
        textRect = text.get_rect()
        textRect.center = (x, y)
  
        screen.blit(text, textRect)
  
    def getRect(self):
        return self.playerRect

class Ball:
    def __init__(self, posx, posy, radius, speed, color):
        self.posx = posx
        self.posy = posy
        self.radius = radius
        self.speed = speed
        self.color = color
        self.xFac = 1
        self.yFac = -1
        self.ball = pg.draw.circle(
            screen, self.color, (self.posx, self.posy), self.radius)
        self.firstTime = 1
  
    def display(self):
        self.ball = pg.draw.circle(
            screen, self.color, (self.posx, self.posy), self.radius)
  
    def update(self):
        self.posx += self.speed*self.xFac
        self.posy += self.speed*self.yFac
  
        # If the ball hits the top or bottom surfaces,
        # then the sign of yFac is changed and it
        # results in a reflection
        if self.posy <= 0 or self.posy >= HEIGHT:
            self.yFac *= -1
  
        # If the ball touches the left wall for the first time,
        # The firstTime is set to 0 and we return 1
        # indicating that player2 has scored
        # firstTime is set to 0 so that the condition is
        # met only once and we can avoid giving multiple
        # points to the player
        if self.posx <= 0 and self.firstTime:
            self.firstTime = 0
            return 1
        elif self.posx >= WIDTH and self.firstTime:
            self.firstTime = 0
            return -1
        else:
            return 0
  
    # Used to reset the position of the ball
    # to the center of the screen
    def reset(self):
        self.posx = WIDTH//2
        self.posy = HEIGHT//2
        self.xFac *= -1
        self.firstTime = 1
  
    # Used to reflect the ball along the X-axis
    def hit(self):
        self.xFac *= -1
  
    def getRect(self):
        return self.ball
    
class AI:
      
    # Take the initial position,
    # dimensions, speed and color of the object
    def __init__(self, posx, posy, width, height, color):
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.speed = 5
        self.color = color
        # Rect that is used to control the
        # position and collision of the object
        self.playerRect = pg.Rect(posx, posy, width, height)
        # Object that is blit on the screen
        self.player = pg.draw.rect(screen, self.color, self.playerRect)
  
    # Used to display the object on the screen
    def display(self):
        self.player = pg.draw.rect(screen, self.color, self.playerRect)
  
    # Used to update the state of the object
    # yFac represents the direction of the striker movement
    # if yFac == -1 ==> The object is moving upwards
    # if yFac == 1 ==> The object is moving downwards
    # if yFac == 0 ==> The object is not moving
    def update(self, yFac):
        self.posy = self.posy + self.speed*yFac
  
        # Restricting the striker to be below
        # the top surface of the screen
        if self.posy <= 0:
            self.posy = 0
        # Restricting the striker to be above
        # the bottom surface of the screen
        elif self.posy + self.height >= HEIGHT:
            self.posy = HEIGHT-self.height
  
        # Updating the rect with the new values
        self.playerRect = (self.posx, self.posy, self.width, self.height)
  
    # Used to render the score on to the screen
    # First, create a text object using the font.render() method
    # Then, get the rect of that text using the get_rect() method
    # Finally blit the text on to the screen
    def displayScore(self, text, score, x, y, color):
        text = font20.render(text+str(score), True, color)
        textRect = text.get_rect()
        textRect.center = (x, y)
  
        screen.blit(text, textRect)
  
    def getRect(self):
        return self.playerRect

