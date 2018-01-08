import pygame
from pygame.locals import *

#pygame initialization
pygame.init()


##########################################################################
############################# VARIABLES ##################################
screen_size=(640,480)
player_size=(int(screen_size[0]/10),int(screen_size[1]/10))
player_pos=(0, 0)


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
screen.blit(pygame.transform.scale(player_image, player_size), player_pos)

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
			player_size=(int(screen_size[0]/10),int(screen_size[1]/10))			
			screen = pygame.display.set_mode(screen_size, RESIZABLE)
			#update images size
			screen.blit(pygame.transform.scale(background, screen_size), (0, 0))
			screen.blit(pygame.transform.scale(player_image, player_size), player_pos)
			#refresh display
			pygame.display.flip()
		if event.type == KEYDOWN : #if user press a key
			if event.key == K_RIGHT: #right
				#move player position if he doesn't go outside the window
				if player_pos[0]+player_size[0]< screen_size[0]-player_size[0]:
					player_pos=(player_pos[0]+player_size[0], player_pos[1])
				else:
					player_pos=(screen_size[0]-player_size[0], player_pos[1])
				#redisplay background to remove previous player's image
				screen.blit(pygame.transform.scale(background, screen_size), (0, 0))
				#display player's image on the new position
				screen.blit(pygame.transform.scale(player_image, player_size), player_pos)
				#refresh display
				pygame.display.flip()
			if event.key == K_LEFT: #LEFT
				#move player position if he doesn't go outside the window
				if player_pos[0]-player_size[0]> 0:
					player_pos=(player_pos[0]-player_size[0], player_pos[1])
				else:
					player_pos=(0, player_pos[1])				
				#redisplay background to remove previous player's image
				screen.blit(pygame.transform.scale(background, screen_size), (0, 0))
				#display player's image on the new position
				screen.blit(pygame.transform.scale(player_image, player_size), player_pos)
				#refresh display
				pygame.display.flip()
			if event.key == K_DOWN: #DOWN
				#move player position if he doesn't go outside the window
				if player_pos[1]+player_size[1]< screen_size[1]-player_size[1]:
					player_pos=(player_pos[0], player_pos[1]+player_size[1])
				else:
					player_pos=(player_pos[0], screen_size[1]-player_size[1])
				#redisplay background to remove previous player's image
				screen.blit(pygame.transform.scale(background, screen_size), (0, 0))
				#display player's image on the new position
				screen.blit(pygame.transform.scale(player_image, player_size), player_pos)
				#refresh display
				pygame.display.flip()
			if event.key == K_UP: #UP
				#move player position if he doesn't go outside the window
				if player_pos[1]-player_size[1]> 0:
					player_pos=(player_pos[0], player_pos[1]-player_size[1])
				else:
					player_pos=(player_pos[0], 0)				
				#redisplay background to remove previous player's image
				screen.blit(pygame.transform.scale(background, screen_size), (0, 0))
				#display player's image on the new position
				screen.blit(pygame.transform.scale(player_image, player_size), player_pos)
				#refresh display
				pygame.display.flip()

