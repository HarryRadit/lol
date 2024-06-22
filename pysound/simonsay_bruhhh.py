# Import required modules
import pygame
import sys
import math
import random


#initialize the pygame library
pygame.init()

#set up the game window dimensions
window_width,window_height = 400,300
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Simon says')

BRAINROT = {
    1 : {
        'image' : pygame.transform.scale(pygame.image.load('download(6).png'), (50, 100)),
        'sound' : pygame.mixer.Sound('amogus-sound.mp3')

},
    2 : {
        'image' : pygame.transform.scale(pygame.image.load('download (16).jpeg'), (50, 100)),
        'sound' : pygame.mixer.Sound('bye-bye-mewing_fMVssQz.mp3')
    },
    3 : {
        'image' : pygame.transform.scale(pygame.image.load('download (17).jpeg'), (50, 100)),
        'sound' : pygame.mixer.Sound('you-are-my-sunshine-lebron-james.mp3')
    },
    4: {
        'image' : pygame.transform.scale(pygame.image.load('download (18).jpeg'), (50, 100)),
        'sound' : pygame.mixer.Sound('metal-pipe-clang.mp3')
    }

}
"""
BRAINROT[4]['sound'].play()
pygame.time.delay(2000)
"""

#list to store the sequence
sequence = []

#function to display message on the screen
def display_message(message):
    font = pygame.font.SysFont(None, 48)
    text = font.render(message, True, (255, 255, 255))
    text_rect = text.get_rect(center = (window_width // 2, window_height // 4))
    window.fill((255,255,255))
    window.blit(text, text_rect)
    pygame.display.update()

#function to display the superhero image
def display_image():
    for i in range(1,5):
        window.blit(BRAINROT[i]['image'],((i-1)*100+25,150))
    pygame.display.update()

#function to play the sequence of sounds and images

def play_sequence(length):
    global sequence
    sequence = [random.randint(1,4) for _ in range(length)]
    display_message("listen sequence")


    for BRAINROT_num in sequence:
        BRAINROT[BRAINROT_num]['sound'].play()
        display_image()



def play_sound_end_get_response():
    global sequence
    sequence_length = len(sequence)+1
    play_sequence(sequence_length)

    #wait for player response
    for BRAINROT_num in sequence:
        waiting_for_input = True
        while  waiting_for_input:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    image_rect = BRAINROT[BRAINROT_num]['image'].get_rect(
                        topleft =  ((BRAINROT_num-1)*100+25,150)
                    )
                    if image_rect.collidepoint(mouse_x, mouse_y):
                        waiting_for_input = False
                    else:
                        return False  #wrong sequence, gameover

    return True

pygame.mixer.init()

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    #play sound and get player response
    if play_sound_end_get_response():
        display_message("correct sequence")
        print("correct sequence")
        pygame.time.delay(1500)
    else:
        display_message("wrong sequence")
        print("wrong sequence")
        pygame.time.delay(2000)
        game_over = True

pygame.quit()
sys.exit()