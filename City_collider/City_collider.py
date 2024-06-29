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
car_img = pygame.image.load('download (15).jpeg').convert_alpha()
car_width, car_height = car_img.get_size()
car_scale = 0.15
car_img = pygame.transform.scale(car_img, (int(car_width*car_scale), int(car_height*car_scale)))

#car position
car_x = window_width // 2 - car_width // 2
car_y = window_height - 50
car_speed = 3

class Asteroid:
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

anothercar_img = pygame.image.load("download (6).png").convert_alpha()
anothercar_width, anothercar_height = anothercar_img.get_size()

max_anothercar_scale = 0.15
min_anothercar_scale = 0.05

anothercar = []
clock = pygame.time.Clock()
game_running = True

def close_game():
    pygame.quit()
    sys.exit()

#f to update the background position for scrolling

def update_background():
    global background1_y, background2_y
    background1_y = (background1_y + 1) % window_height
