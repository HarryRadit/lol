import pygame, sys
from pygame.locals import QUIT, MOUSEBUTTONDOWN

pygame.init()

window_width, window_height = 400,300
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Ping Pong")

#colors

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

#PADDLE

paddle_width = 10
paddle_height = 50

paddle_x = window_width / 2 - paddle_width / 2

paddle_y = window_height - paddle_height
#BALL

ball_x = window_width // 2

ball_y = window_height // 2

ball_radius = 10
ball_x = 3
ball_y = -3

#score
score = 0

font = pygame.font.SysFont(None, 48)

game_over = False

while not game_over:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    #draw everything

    window.fill(white)
    paddle = pygame.draw.rect(window, black, (paddle_x, paddle_y, paddle_height, paddle_width))
    ball = pygame.draw.circle(window, black, (ball_x + 200, ball_y +240), ball_radius)

    pygame.display.update()


