import pygame
import random
import time

pygame.init()

display_width = 800
display_height = 600
car_width = 128

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

gameDisplay = pygame.display.set_mode((display_width, display_height)) #Sets game window
pygame.display.set_caption('Racing Game')

clock = pygame.time.Clock() #Sets game clock

car_image = pygame.image.load('car-from-top-hi.png')

def road_object(road_objectX, road_objectY, road_objectW, road_objectH, color):
	pygame.draw.rect(gameDisplay, color, [road_objectX, road_objectY, road_objectW, road_objectH])

def crash(): #Displays message at the end of the game
	message_display('You Crashed')

def message_display(text): #Generates the end game message
	largeText = pygame.font.Font('freesansbold.ttf', 115)
	TextSurf, TextRect = text_objects(text, largeText)
	TextRect.center = ((display_width/2), (display_height/2))
	gameDisplay.blit(TextSurf, TextRect)

	pygame.display.update()
	time.sleep(2)

	game_loop()

def text_objects(text, font):
	textSurface = font.render(text, True, red)
	return textSurface, textSurface.get_rect()

def car(x,y): #Function defines the car and where it will be displayed
	gameDisplay.blit(car_image,(x,y))

def game_loop(): #Needed for game functionality
	x = (display_width * 0.45)
	y = (display_height * 0.70)

	x_change = 0

	road_objectStartX = random.randrange(0, display_width)
	road_objectStartY = -600 
	road_objectSpeed = 7 
	road_objectWidth = 100
	road_objectHeight = 100

	gameExit = False #End game var

	while not gameExit:  #Starts the game loop
		for event in pygame.event.get():  #Captures the game events
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_change = -5
				elif event.key == pygame.K_RIGHT:
					x_change = 5

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change = 0

			print(event)  #Prints events as they happen	

		x += x_change #Sets the new x based on the event
		pygame.display.update()
		gameDisplay.fill(white)
		road_object(road_objectStartX, road_objectStartY, road_objectWidth, road_objectHeight, black)
		road_objectStartY += road_objectSpeed
		car(x, y)

		if x > display_width-car_width or x < 0:
			crash()
		if road_objectStartY > display_height:
			road_objectStartY = 0 - road_objectHeight
			road_objectStartX = random.randrange(0, display_width)

		clock.tick(60)

game_loop()
pygame.quit()
quit()

