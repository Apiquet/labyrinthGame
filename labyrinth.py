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

#display background
pygame.display.flip()


continuer = 1

#infinite loop
while continuer:
	continuer = int(input()) 