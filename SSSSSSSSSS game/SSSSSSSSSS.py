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
red = (255, 0, 0)

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
    font_large = pygame.font.Font(None, 50)
    font_small = pygame.font.Font(None, 30)

    game_name = font_large.render("SSSSSNAKE GAME",True, black)
    slow_button = font_small.render("SLOW", True, black)
    normal_button = font_small.render("NORMAL", True,black)
    fast_button = font_small.render("FAST", True, black)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            #check for button clicks to set snake's speed
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                print(x, y)
                if 75 <= x <= 275 and 100 <= y <= 180:
                    print("slow")
                    return "slow"
                elif 125 <= x <= 275 and 180 <= y <= 230:
                    print("normal")
                    return "normal"
                elif 125 <= x <= 275 and 240 <= y <= 300:
                    print("fast")
                    return "fast"



        window.fill(white)
        window.blit(game_name, (WIDTH // 2 - game_name.get_width() // 2, HEIGHT // 4 - game_name.get_height() // 2))
        window.blit(slow_button, (WIDTH // 2 - slow_button.get_width() // 2, HEIGHT // 2 - 10))
        window.blit(normal_button, (WIDTH // 2 - normal_button.get_width() // 2, HEIGHT // 2 + 40))
        window.blit(fast_button, (WIDTH // 2 - fast_button.get_width() // 2, HEIGHT // 2 + 90))
        pygame.display.update()

#class Food


class Food:
    def __init__(self):
        self.position = (random.randint(10, WIDTH - 10), random.randint(10, HEIGHT - 10))

    def respawn(self):
        self.position = (random.randint(10, WIDTH - 10), random.randint(10, HEIGHT - 10))

    def get_position(self):
        return self.position

def distance(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)

def main():
    snake_speed = 0
    speed_level = show_intro_screen()

    if speed_level == "slow":
        snake_speed = 7
    elif speed_level == "normal":
        snake_speed = 10
    elif speed_level == "fast":
        snake_speed = 15

    snake = Snake(speed_level)
    food = Food()

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

        #move the snake
        snake.move()
        head = snake.get_head()
        if distance(head, food.get_position()) < 10:
            food.respawn()
            print("food")
            snake.grow()
            score += 1


        window.fill(white)
        for segment in snake.body:
            pygame.draw.rect(window, black, (segment[0], segment[1], 20, 20))
        # draw food
        pygame.draw.rect(window, red, (20, 20, 20, 20))



        #show score
        font = pygame.font.SysFont(None, 24)
        score_text = font.render("Score: " + str(score), True, black)
        window.blit(score_text, (10, 10))


        pygame.display.update()
        clock.tick(snake_speed)





if __name__ == "__main__":
    main()







