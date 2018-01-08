import pygame
from pygame.locals import *

#pygame initialization
pygame.init()


##########################################################################
############################# VARIABLES ##################################
screen_size=(640,480)
player_size_coeff=7
player_size=(int(screen_size[0]/player_size_coeff),int(screen_size[1]/player_size_coeff))
player_move_coeff=0.1


##########################################################################
########################## SCREEN CREATION ###############################
#creation of the window
screen = pygame.display.set_mode(screen_size, RESIZABLE)

#background
background = pygame.image.load("images/background.jpg").convert()

#player's image
player_image = pygame.image.load("images/titeuf_beginning.png").convert()
#ref the player's position
player_pos=player_image.get_rect()
pygame.key.set_repeat(30, 30)


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
			player_size=(int(screen_size[0]/player_size_coeff),int(screen_size[1]/player_size_coeff))			
			screen = pygame.display.set_mode(screen_size, RESIZABLE)
		if event.type == KEYDOWN : #if user press a key
			if event.key == K_RIGHT: #right
				#move player position if he doesn't go outside the window
				#player's image
				player_image = pygame.image.load("images/titeuf_right.jpg").convert()
				if player_pos.x+player_move_coeff*player_size[0]< screen_size[0]-player_size[0]:
					player_pos=player_pos.move(player_move_coeff*player_size[0],0)
				else:
					player_pos.x=screen_size[0]-player_size[0]				
			if event.key == K_LEFT: #LEFT
				#player's image
				player_image = pygame.image.load("images/titeuf_left.jpg").convert()
				#move player position if he doesn't go outside the window
				if player_pos.x-player_move_coeff*player_size[0]> 0:
					player_pos=player_pos.move(-player_move_coeff*player_size[0],0)
				else:
					player_pos.x=0
			if event.key == K_DOWN: #DOWN
				#player's image
				player_image = pygame.image.load("images/titeuf_down.gif").convert()
				#move player position if he doesn't go outside the window
				if player_pos.y+player_move_coeff*player_size[1]< screen_size[1]-player_size[1]:
					player_pos=player_pos.move(0,player_move_coeff*player_size[1])
				else:
					player_pos.y=screen_size[1]-player_size[1]
			if event.key == K_UP: #UP
				#player's image
				player_image = pygame.image.load("images/titeuf_up.gif").convert()
				#move player position if he doesn't go outside the window
				if player_pos.y-player_move_coeff*player_size[1] > 0:
					player_pos=player_pos.move(0,-player_move_coeff*player_size[1])
				else:
					player_pos[1]=0
		if event.type == MOUSEBUTTONDOWN:
			if event.button == 1:	#if left click
				#player go to click position
				player_pos.x = event.pos[0]
				player_pos.y = event.pos[1]


	#make transparent the background of the image
	player_image.set_colorkey((255,255,255))
	#redisplay background to remove previous player's image
	screen.blit(pygame.transform.scale(background, screen_size), (0, 0))
	#display player's image on the new position
	screen.blit(pygame.transform.scale(player_image, player_size), player_pos)
	#refresh display
	pygame.display.flip()

