import pygame
from pygame.locals import QUIT

pygame.init()
pygame.display.set_caption("PAINTT")

WIDTH = 400
HEIGHT = 300
toolbar_height = 50

#color

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)

#create the window
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

#VARIABLE
drawing = False
brush_size = 2
min_brush_size = 1
max_brush_size = 50
brush_color = BLACK
erase_node = False
last_pos = None

#create a surface for drawing
surface = pygame.Surface((WIDTH, HEIGHT - toolbar_height))
surface.fill(WHITE)

#create the toolbar
toolbar = pygame.Surface((WIDTH, toolbar_height))
toolbar.fill(GREY)

running = True
while running:
    toolbar.fill(GREY)
    font = pygame.font.SysFont(None, 24)
    pen_text = font.render("Pen", True, BLACK)
    erase_text = font.render("Erase", True, BLACK)
    clear_text = font.render("Clear", True, BLACK)
    decrease_text = font.render("-", True, BLACK)
    increase_text = font.render("+", True, BLACK)

    toolbar.blit(pen_text, (40, 20))
    toolbar.blit(erase_text, (80, 20))
    toolbar.blit(clear_text, (120, 20))
    toolbar.blit(decrease_text, (160, 20))
    toolbar.blit(increase_text, (200, 20))


    WINDOW.fill(WHITE)
    WINDOW.blit(surface, (0, toolbar_height))
    WINDOW.blit(toolbar, (0, 0))
