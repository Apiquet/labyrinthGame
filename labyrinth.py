import pygame
from pygame.locals import *

#pygame initialization
pygame.init()


##########################################################################
############################# VARIABLES ##################################
screen_size=(640,480)
player_image_size=(int(screen_size[0]/10),int(screen_size[1]/10))


##########################################################################
########################## SCREEN CREATION ###############################
#creation of the window
screen = pygame.display.set_mode(screen_size, RESIZABLE)

#background
background = pygame.image.load("images/background.jpg").convert()
#adaptation of the image size to the window
screen.blit(pygame.transform.scale(background, screen_size), (0, 0))

#player's image
player_image = pygame.image.load("images/worm.jpg").convert()
#make transparent the background of the image
player_image.set_colorkey((255,255,255))
#adaptation of the image size to the window
screen.blit(pygame.transform.scale(player_image, (int(screen_size[0]/10),int(screen_size[1]/10))), (0, 0))

#Refresh the display
pygame.display.flip()

continuer = 1

##########################################################################
################################ GAME ####################################
#infinite loop
while continuer:
	for event in pygame.event.get():   #verify events
		if event.type == QUIT:     #if user want to QUIT
			continuer = 0      #Stop the loop
		if event.type == VIDEORESIZE:	#if user resize screen
			#update screen size
			screen_size=(event.w, event.h)			
			screen = pygame.display.set_mode(screen_size, RESIZABLE)
			#update images size
			screen.blit(pygame.transform.scale(background, screen_size), (0, 0))
			screen.blit(pygame.transform.scale(player_image, (int(screen_size[0]/10),int(screen_size[1]/10))), (0, 0))
			#refresh display
			pygame.display.flip()