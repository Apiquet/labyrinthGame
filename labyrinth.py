import pygame
from pygame.locals import *

#pygame initialization
pygame.init()


##########################################################################
############################# VARIABLES ##################################
screen_size=(910,700)
player_size_coeff=6
player_size=(int(screen_size[0]/player_size_coeff),int(screen_size[1]/player_size_coeff))
player_move_coeff=0.25


##########################################################################
########################## SCREEN CREATION ###############################
#creation of the window
screen = pygame.display.set_mode(screen_size)

#background
labyrinth = pygame.image.load("images/background2.jpg").convert()
background = pygame.image.load("images/background.jpg").convert()

#player's image
player_image = pygame.image.load("images/titeuf_right.jpg").convert()
#Nadia's image
nadia = pygame.image.load("images/Nadia.jpg").convert()
#Nadia and Titeuf
nadia_titeuf = pygame.image.load("images/nadia_titeuf.png").convert()
#ref the player's position
player_pos=player_image.get_rect()
nadia_pos=nadia.get_rect()

pygame.key.set_repeat(1, 1)

continuer = 1

##########################################################################
################################ GAME ####################################
#infinite loop
while continuer:
	for event in pygame.event.get():   #verify events
		if event.type == QUIT:     #if user want to QUIT
			continuer = 0      #Stop the loop
		'''if event.type == VIDEORESIZE:	#if user resize screen
			#update screen size
			screen_size=(event.w, event.h)
			player_size=(int(screen_size[0]/player_size_coeff),int(screen_size[1]/player_size_coeff))			
			screen = pygame.display.set_mode(screen_size)'''
		if event.type == KEYDOWN : #if user press a key
			if event.key == K_RIGHT: #right
				#move player position if he doesn't go outside the window
				#player's image
				player_image = pygame.image.load("images/titeuf_right.jpg").convert()
				if player_pos.x+player_move_coeff*player_size[0]< screen_size[0]-player_size[0]:
					if (player_pos.y<53 and player_pos.x<432) or (player_pos.y>444):
						player_pos=player_pos.move(player_move_coeff*player_size[0],0)
				else:
					player_pos.x=screen_size[0]-player_size[0]				
			if event.key == K_LEFT: #LEFT
				#player's image
				player_image = pygame.image.load("images/titeuf_left.jpg").convert()
				#move player position if he doesn't go outside the window
				if player_pos.x-player_move_coeff*player_size[0]> 0:
					if (player_pos.y<53 and player_pos.x<462) or (player_pos.y>444):
						player_pos=player_pos.move(-player_move_coeff*player_size[0],0)
				else:
					player_pos.x=0
			if event.key == K_DOWN: #DOWN
				#player's image
				player_image = pygame.image.load("images/titeuf_down.gif").convert()
				#move player position if he doesn't go outside the window
				if player_pos.y+player_move_coeff*player_size[1]< screen_size[1]-player_size[1]:
					if (player_pos.x>310 and player_pos.x<462) or player_pos.x>663:
						player_pos=player_pos.move(0,player_move_coeff*0.7*player_size[1])
				else:
					player_pos.y=screen_size[1]-player_size[1]
			if event.key == K_UP: #UP
				#player's image
				player_image = pygame.image.load("images/titeuf_up.gif").convert()
				#move player position if he doesn't go outside the window
				if player_pos.y-player_move_coeff*player_size[1] > 0:
					if (player_pos.x>310 and player_pos.x<462) or player_pos.x>663:
						player_pos=player_pos.move(0,-player_move_coeff*0.7*player_size[1])
				else:
					player_pos[1]=0
		if event.type == MOUSEBUTTONDOWN:
			if event.button == 1:	#if left click
				#player go to click position
				print(event.pos[0])
				print(event.pos[1])


	#make transparent the background of the image
	labyrinth.set_colorkey((255,255,255))
	screen.blit(pygame.transform.scale(background, screen_size), (0, 0))
	screen.blit(pygame.transform.scale(labyrinth, screen_size), (0, 0))
	
	if (player_pos.x>screen_size[0]-player_size[0]*1.5) and (player_pos.y<nadia_pos.y + player_size[1]):
		#make transparent backkground
		nadia_titeuf.set_colorkey((255,255,255))
		#display player's image on the new position
		screen.blit(pygame.transform.scale(nadia_titeuf, player_size), (screen_size[0]-player_size[0]*1.2,0))
	else:	
		#make transparent backkground	
		player_image.set_colorkey((255,255,255))		
		nadia.set_colorkey((255,255,255))
		#display player's image on the new position
		screen.blit(pygame.transform.scale(player_image, player_size), player_pos)
		screen.blit(pygame.transform.scale(nadia, player_size), (screen_size[0]-player_size[0],0))
		

	#refresh display
	pygame.display.flip()

