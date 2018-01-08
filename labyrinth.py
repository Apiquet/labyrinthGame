import pygame
from pygame.locals import *

#pygame initialization
pygame.init()

#creation of the window
fenetre = pygame.display.set_mode((640,480), RESIZABLE)

#background
fond = pygame.image.load("images/background.jpg").convert()
#adaptation of the image size to the window
fenetre.blit(pygame.transform.scale(fond, (640, 480)), (0, 0))

#player's image
player_image = pygame.image.load("images/worm.jpg").convert()
#make transparent the background of the image
player_image.set_colorkey((255,255,255))
#adaptation of the image size to the window
fenetre.blit(pygame.transform.scale(player_image, (50, 50)), (0, 0))

#Refresh the display
pygame.display.flip()


continuer = 1

#infinite loop
while continuer:
	continuer = int(input()) 