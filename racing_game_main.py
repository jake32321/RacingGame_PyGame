import pygame 

pygame.init()

gameDisplay = pygame.display.set_mode((800, 600)) #Sets game window
pygame.display.set_caption('Racing Game')

clock = pygame.time.Clock() #Sets game clock

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

