import pygame as pg
from sprites import *
from settings import *


def main():
    running = True
    # Defining the objects
    player1 = Paddle(20, 0, 10, 100, 10, WHITE)
    player2 = AI(WIDTH-30, 0, 10, 100, 20, WHITE)
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
            if event.type == pg.K_r:
                reset()
                print("uhh")
            if event.type == pg.K_9:
                hard_mode()
                print("hi")
            if event.type == pg.K_8:
                normal_mode()
                print("hello")
            if event.type == pg.K_7:
                easy_mode()
                print("yo")
            if event.type == pg.KEYUP:
                if event.key == pg.K_w or event.key == pg.K_s:
                    player1YFac = 0
                
  
        # Collision detection
        for player in listOfPlayers:
            if pg.Rect.colliderect(ball.getRect(), player.getRect()):
                ball.hit()
        
        def reset():
            player1 = Paddle(20, 0, 10, 100, 10, WHITE)
            player2 = Paddle(WIDTH-30, 0, 10, 100, 20, WHITE)
            ball = Ball(WIDTH//2, HEIGHT//2, 7, 7, WHITE)
            player1Score, player2Score = 0, 0
            player1YFac, player2YFac = 0, 0
            ball.reset()
            
        def hard_mode():
            player2.posy = ball.posy 
        def easy_mode():
            player2.posy = ball.posy - 10     
        def normal_mode():
            player2.posy = ball.posy - 5
  
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
        player1.displayScore("Player : ", player1Score, 100, 20, WHITE)
        player2.displayScore("Computer : ", player2Score, WIDTH-100, 20, WHITE)

        
        # win/lose screen
        if player1Score >= 3:
            screen.fill(BLACK)
            draw_text("You Win", 55, GREEN, WIDTH/2, HEIGHT/3)
            
        if player2Score >= 3:
            screen.fill(BLACK)
            draw_text("You Lose", 55, RED, WIDTH/2, HEIGHT/3)
            
  
        pg.display.update()
        
        # Adjusting the frame rate
        clock.tick(FPS)
        # drawing the text
        def draw_text (text, size, color, x, y):
            font_name = pg.font.match_font('comic sans')
            font = pg.font.Font(font_name, size)
            text_surface = font.render(text, True, color)
            text_rect = text_surface.get_rect()
            text_rect.midtop = (x,y)
            screen.blit(text_surface, text_rect)


