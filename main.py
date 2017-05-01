import pygame
import time
import random

pygame.init()

white = (255,255,255)
black  = (0,0,0)
red = (255,0,0)
green = (0,155,0)

display_width = 800
display_height = 600

block_size = 20

FPS = 20

direction = "right"

smallfont = pygame.font.SysFont("arialms  ",25)
medfont = pygame.font.SysFont("arialms  ",50)
largefont = pygame.font.SysFont("arialms  ",80)

	
def game_intro():
	intro = True
	while intro :
		for event in pygame.event.get():	
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_c:
					intro = False
				if event.key == pygame.K_q:
					pygame.quit()
					quit()
				
			
		gameDisplay.fill(black)
		message_to_screen("Welcome to your Doom",red,-100,"large")
		message_to_screen("Eat the fucking apples m8",white,-30)
		message_to_screen("Eat moar get moar fat", white,10)
		message_to_screen("C para continuar ou Q para sair", white,50)

		pygame.display.update()
		clock.tick(15)

def cav (snakelist,block_size):
	if direction == "right":
		head = knight
	if direction == "left":
		head = pygame.transform.rotate(img , 90)

	gameDisplay.blit(knight, ())
	

def text_objetcs (text , color,size):
	if size == 'small':
		txtSurf = smallfont.render(text , True , color)
	elif size == 'medium':
		txtSurf = medfont.render(text , True , color)
	elif size == 'large':
		txtSurf = largefont.render(text , True , color)
	return txtSurf , txtSurf.get_rect()	
		
def message_to_screen (msg,color,y_displace=0,size = "small"):
	#screen_text = font.render(msg,True,color)
	#gameDisplay.blit(screen_text,[display_width/2,display_height/2])
	
	txtSurf , txtRect = text_objetcs(msg , color,size)
	txtRect.center = (display_width/2 ),(display_height/2)+y_displace
	gameDisplay.blit(txtSurf , txtRect)
	
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Dungeon Runners")
icon = pygame.image.load('knight.png')
pygame.display.set_icon(icon)
pygame.display.update()


knight = pygame.image.load('knight.png')
appleThickness = 30
clock = pygame.time.Clock()

def gameLoop():
	global direction
	
	appleThickness = 30
	
	direction = 'right'
	gameExit = False
	gameOver = False

	lead_x = display_width/2
	lead_y = display_height/2
	lead_x_change = 0
	lead_y_change = 0
	
	
	while not gameExit:
	
		while gameOver == True:
			gameDisplay.fill(black)
			message_to_screen("GAME OVER",red,size = 'large')
			message_to_screen("C para continuar ou Q para sair",white, -50,size = 'medium')
			
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:	
					gameExit = True
					gameOver = False
				if event.type == pygame.KEYDOWN:
					if event.key  == pygame.K_q:
						gameExit = True
						gameOver = False
					if event.key  == pygame.K_c:
						gameLoop()
			
			pygame.display.update()

		for event in pygame.event.get():
			#print(event)
			if event.type == pygame.QUIT:
				gameExit = True 
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					direction = "left"
					lead_x_change = -appleThickness
				if event.key == pygame.K_RIGHT:
					direction = "right"
					lead_x_change = appleThickness
				if event.key == pygame.K_UP:
					direction = "up"
					lead_y_change = -appleThickness
				if event.key == pygame.K_DOWN:
					direction = "down"
					lead_y_change = -appleThickness
		
		lead_x += lead_x_change
		lead_y += lead_y_change
		
		gameDisplay.blit(knight,(display_width/2 ),(display_height/2))
		
		if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0 :
			gameOver = True
				
	
		gameDisplay.fill(white)	
	
		
		#pygame.draw.rect(gameDisplay ,white, [randAppleX,randAppleY ,appleThickness,appleThickness])

	
			
	
		
		pygame.display.update()
		

		# if lead_x>= randAppleX and lead_x <= randAppleX + appleThickness:
			# if lead_y>= randAppleY and lead_y <= randAppleY + appleThickness:
				# randAppleX = round(random.randrange(0,display_width-block_size))#/10.0)*10	
				# randAppleY = round(random.randrange(0, display_height-block_size))#/10.0)*10
				# snakeLenght += 1
		
		#colisao
	
				
				
		clock.tick(FPS)
		
	pygame.quit()
	quit()
	
game_intro()
gameLoop()