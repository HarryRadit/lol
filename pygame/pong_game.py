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
ball_speedx = 3
ball_speedy= -3

#score
score = 0

font = pygame.font.SysFont(None, 48)

game_over = False

while not game_over:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        #move the paddle
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] and paddle_x > 0:
            paddle_x += 5
        if keys[pygame.K_a] and paddle_x < window_width - paddle_width:
            paddle_x -= 5

        #move the ball
        ball_x += ball_speedx
        ball_y += ball_speedy



    #draw everything

    window.fill(white)
    paddle = pygame.draw.rect(window, black, (paddle_x, paddle_y, paddle_height, paddle_width))
    ball = pygame.draw.circle(window, black, (ball_x , ball_y ), ball_radius)

    score_text = font.render("Score: " + str(score), True, black)
    window.blit(score_text, (10, 10))

    pygame.display.update()


    # ball collsion with walls
    if ball.left <= 0 or ball.right >= window_width:
        ball_speedx *= -1
    if ball.top <= 0 or ball.bottom >= window_height:
        ball_speedy *= -1

    #ball collsion with paddle
    if pygame.Rect.colliderect(ball,paddle):
        ball_speedy *= -1
        score += 100000

    if ball.bottom >= window_height:
        game_over = True
window.fill(red)
score_text = font.render("Score: " + str(score), True, black)
window.blit(score_text, (10, 10))
game_over_text = font.render("Game Over", True, black)
window.blit(game_over_text, (window_width // 2 - 100, window_height // 2))
pygame.display.update()

pygame.time.delay(2000)
pygame.quit()
sys.exit()



pygame.display.update()
pygame.time.delay(30)

pygame.quit()
sys.exit()

