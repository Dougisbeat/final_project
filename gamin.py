import pygame as pg
from sprites import *
from settings import *
def main():
    running = True
  
    # Defining the objects
    player1 = Paddle(20, 0, 10, 100, 10, WHITE)
    player2 = AI(WIDTH-30, 0, 10, 100, WHITE)
    ball = Ball(WIDTH//2, HEIGHT//2, 7, 7, WHITE)
  
    listOfPlayers = [player1, player2]
  
    # Initial parameters of the players
    player1Score, player2Score = 0, 0
    player1YFac, player2YFac = 0, 0
  
    while running:
        screen.fill(BLACK)
        # background
        screen.blit(background, (0,0))

        player2.posy = ball.posy
        # Event handling
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_w:
                    player1YFac = -1
                if event.key == pg.K_s:
                    player1YFac = 1
            if event.type == pg.KEYUP:
                if event.key == pg.K_w or event.key == pg.K_s:
                    player1YFac = 0
  
        # Collision detection
        for player in listOfPlayers:
            if pg.Rect.colliderect(ball.getRect(), player.getRect()):
                ball.hit()
  
        # Updating the objects
        player1.update(player1YFac)
        player2.update(player2YFac)
        point = ball.update()
  
        # -1 -> player_1 has scored
        # +1 -> player_2 has scored
        #  0 -> None of them scored
        if point == -1:
            player1Score += 1
        elif point == 1:
            player2Score += 1
  
        if point:   # Someone has scored a point and the
          # ball is out of bounds. So, we reset it's position
            ball.reset()
  
        # Displaying the objects on the screen
        player1.display()
        player2.display()
        ball.display()
  
        # Displaying the scores of the players
        player1.displayScore("player_1 : ", player1Score, 100, 20, WHITE)
        player2.displayScore("player_2 : ", player2Score, WIDTH-100, 20, WHITE)
  
        pg.display.update()
        # Adjusting the frame rate
        clock.tick(FPS)

def title():
    