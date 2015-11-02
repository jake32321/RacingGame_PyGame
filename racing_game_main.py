import pygame 

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

gameDisplay = pygame.display.set_mode((display_width, display_height)) #Sets game window
pygame.display.set_caption('Racing Game')

clock = pygame.time.Clock() #Sets game clock

car_image = pygame.image.load('car.png')

crashed = False #End game var

while not crashed:  #Starts the game loop
	for event in pygame.event.get():  #Captures the game events
		if event.type == pygame.QUIT:
			crashed = True

		print(event)  #Prints events as they happen

	pygame.display.update()
	clock.tick(60)

pygame.quit()
quit()

