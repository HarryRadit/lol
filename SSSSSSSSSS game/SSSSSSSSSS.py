import pygame
import time
import random
import math

pygame.init()

WIDTH, HEIGHT = 400, 300
window_size = (WIDTH, HEIGHT)
window_title = "SSSSNAKE GAME"

white = (255, 255, 255)
black = (0, 0, 0)

#create the game window
window = pygame.display.set_mode(window_size)
pygame.display.set_caption(window_title)

#snake class to manage movement and growth
class Snake:
    def __init__(self, speed):
        self.body = [(WIDTH // 2, HEIGHT // 2) for i in range(4)]
        self.direction = (1, 0)
        self.speed = speed

    def move(self):
        dx, dy = self.direction
        new_head = ((self.body[0][0] + dx * 20) % WIDTH, (self.body[0][1] + dy * 20) % HEIGHT)
        self.body.pop()
        self.body.insert(0, new_head)

    def grow(self):
        dx, dy = self.direction
        new_tail = ((self.body[-1][0] + dx * 20) % WIDTH, (self.body[-1][1] + dy * 20) % HEIGHT)
        self.body.append(new_tail)

    def change_direction(self, dx, dy):
        if (dx, dy) != (-self.direction[0], -self.direction[1]):
            self.direction = (dx, dy)

    def get_head(self):
        return self.body[0]

    def get_body(self):
        return self.body

    def set_speed(self, speed):
        self.speed = speed


#show intro screen
def show_intro_screen():
    font_large = pygame.font.Font(name=None, size=50)
    font_small = pygame.font.Font(name=None, size=30)

    game_name = font_large.render(text="SSSSSNAKE GAME", color=black)
    slow_button = font_small.render(text="SLOW", color=black)
    normal_button = font_small.render(text="NORMAL", color=black)
    fast_button = font_small.render(text="FAST", color=black)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            #check for button clicks to set snake's speed
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                if 125 <= x <= 275 and 350 <= y <= 200:
                    return "slow"
                elif 125 <= x <= 275 and 250 <= y <= 250:
                    return "normal"
                elif 125 <= x <= 275 and 250 <= y <= 300:
                    return "fast"



        window.fill(white)
        window.blit(game_name, (WIDTH // 2, HEIGHT // 4 - game_name.get_width() // 2))
        window.blit(slow_button, (WIDTH // 2 - slow_button.get_width(), HEIGHT // 2 - 10))
        window.blit(normal_button, (WIDTH // 2 - normal_button.get_width(), HEIGHT // 2 - 40))
        window.blit(fast_button, (WIDTH // 2 - fast_button.get_width(), HEIGHT // 2 + 90))
        pygame.display.update()


def main():
    speed_level = show_intro_screen()

    if speed_level == "slow":
        speed = 0.1
    elif speed_level == "normal":
        speed = 10
    elif speed_level == "fast":
        speed = 15

    snake = Snake(speed_level)

    score = 0
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction(0, -1)
                elif event.key == pygame.K_DOWN:
                    snake.change_direction(0, 1)
                elif event.key == pygame.K_LEFT:
                    snake.change_direction(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction(1, 0)

        snake.move()
        if snake.get_head() in snake.get_body()[1:]:
            pygame.quit()
            return

        window.fill(white)







