#module
import pygame
import random
import sys

#initialize the pygame library
pygame.init()

#set up the game window
window_width,window_height = 400, 300
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('City Collider')

#load background image and scale it
background1 = pygame.image.load('empty-road-semi-flat-vector-illustration-top-view-single-drive-way-countryside-straight-city-route-track-path-traffic-line-180839666.jpg').convert()
background1 = pygame.transform.scale(background1, (window_width, window_height))
background2 = pygame.transform.scale(background1, (window_width, window_height))

#load car image
car_img = pygame.image.load('images__6_-removebg-preview.png').convert_alpha()
car_width, car_height = car_img.get_size()
car_scale = 0.15
car_img = pygame.transform.scale(car_img, (int(car_width*car_scale), int(car_height*car_scale)))

#car position
car_x = window_width // 2 - car_width // 2
car_y = window_height - 50
car_speed = 3

class Anothercar:
    def __init__(self, x, y, image, scale):
        self.x = x
        self.y = y
        self.image = image
        self.scale = scale

        #resize the another car image based on the scale
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width()*self.scale), int(self.image.get_height()*self.scale)))

    def move(self,speed):
        self.y += speed

    def draw(self,window):
        window.blit(self.image, (self.x, self.y))

anothercar_img = pygame.image.load("download__15_-removebg-preview.png").convert_alpha()
anothercar_width, anothercar_height = anothercar_img.get_size()

max_anothercar_scale = 0.15
min_anothercar_scale = 0.05

anothercars = []
clock = pygame.time.Clock()
game_running = True

def close_game():
    pygame.quit()
    sys.exit()

#f to update the background position for scrolling

def update_background():
    global background1_y, background2_y
    background1_y = (background1_y + 1) % window_height
    background2_y = background1_y - window_height
    window.blit(background1, (0, background1_y))
    window.blit(background2, (0, background2_y))

background1_y = 0
background2_y = window_height

while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
            close_game()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        car_x -= car_speed
        if car_x < 0:
            car_x = 0
    if keys[pygame.K_RIGHT]:
        car_x += car_speed
        if car_x > window_width:
            car_x = window_width - car_width

    window.fill((0, 0, 0))
    update_background()
    window.blit(car_img, (car_x, car_y))


    #another car spawn
    if random.randint(0,100) < 2:
        anothercar_x = random.randint(60, window_width - 120)
        anothercar_scale = random.uniform(min_anothercar_scale, max_anothercar_scale)
        anothercar = Anothercar(anothercar_x, -int(anothercar_height), anothercar_img, 0.2)
        anothercars.append(anothercar)

    #rectangles to represent the collision of cars
    anothercar_rect = pygame.Rect(car_x, car_y, car_width, car_height)
    
    #move and draw another cars
    for anothercar in anothercars:
        anothercar.move(0.5)
        anothercar_rect = pygame.Rect(anothercar.x, anothercar.y, anothercar_width, anothercar_height)
        anothercar.draw(window)

        if anothercar_rect.colliderect(anothercar_rect):
            #game_running = False
            #close_game()
            pass
    #remove the another cars  that have passed the screen
    anothercars = [anothercar for anothercar in anothercars if anothercar.y < window_height]

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()

