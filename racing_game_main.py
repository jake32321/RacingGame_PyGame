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

car_image = pygame.image.load('car-from-top-hi.png')

def car(x,y): #Function defines the car and where it will be displayed
	gameDisplay.blit(car_image,(x,y))

x = (display_width * 0.45)
y = (display_height * 0.70)

x_change = 0

crashed = False #End game var

while not crashed:  #Starts the game loop
	for event in pygame.event.get():  #Captures the game events
		if event.type == pygame.QUIT:
			crashed = True

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
	car(x, y)
	clock.tick(60)

pygame.quit()
quit()

