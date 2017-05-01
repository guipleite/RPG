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

block_size = 30

FPS = 20

direction = "right"

smallfont = pygame.font.SysFont("arialms  ",25)
medfont = pygame.font.SysFont("arialms  ",50)
largefont = pygame.font.SysFont("arialms  ",80)

# def randAppleGen():
	# randAppleX = round(random.randrange(0,display_width-appleThickness))#/10.0)*10	
	# randAppleY = round(random.randrange(0, display_height-appleThickness))#/10.0)*10
	# return randAppleX , randAppleY

def telas (tela):
	gameDisplay.blit(tela , [0,0])
	
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

def score(score):
	text = smallfont.render("Score: " + str(score),True , white)
	gameDisplay.blit(text,[0,0])
		
def snake (snakelist,block_size):
	if direction == "right":
		head = imgr
	if direction == "left":
		head = imgl
	if direction == "up":
		head = imgr
	if direction == "down":
		head = imgl

	gameDisplay.blit(head,(snakelist[-1][0], snakelist[-1][1]))

def text_objetcs (text , color,size):
	if size == 'small':
		txtSurf = smallfont.render(text , True , color)
	elif size == 'medium':
		txtSurf = medfont.render(text , True , color)
	elif size == 'large':
		txtSurf = largefont.render(text , True , color)
	return txtSurf , txtSurf.get_rect()	
		
def message_to_screen (msg,color,y_displace=0,size = "small"):
	
	txtSurf , txtRect = text_objetcs(msg , color,size)
	txtRect.center = (display_width/2 ),(display_height/2)+y_displace
	gameDisplay.blit(txtSurf , txtRect)
	
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Dungeon Runners")
icon = pygame.image.load('knightr.png')
pygame.display.set_icon(icon)
pygame.display.update()

imgl = pygame.image.load('knightr.png')
imgr = pygame.image.load('knightl.png')
telainicio = pygame.image.load('room.png')
tela2 = pygame.image.load('room2.png')
tela3 = pygame.image.load('room3.png')
tela4 = pygame.image.load('room4.png')
tela5 = pygame.image.load('room4.png')#
tela6 = pygame.image.load('room4.png')#

tela = telainicio
appleThickness = 30
clock = pygame.time.Clock()

def gameLoop():
	global direction
	global tela
	
	appleThickness = 30
	
	direction = 'right'
	gameExit = False
	gameOver = False

	lead_x = display_width/2
	lead_y = display_height/2
	lead_x_change = 10
	lead_y_change = 0
	
	snakelist = []
	snakeLenght = 1
	

	
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
					lead_x_change = -block_size
					lead_y_change = 0
				if event.key == pygame.K_RIGHT:
					direction = "right"
					lead_x_change = block_size
					lead_y_change = 0
				if event.key == pygame.K_UP:
					direction = "up"
					lead_y_change = -block_size
					lead_x_change = 0
				if event.key == pygame.K_DOWN:
					direction = "down"
					lead_y_change = block_size
					lead_x_change = 0
			
			elif event.type == pygame.KEYUP:	
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					lead_x_change = 0
				elif event.key == pygame.K_UP or event.key == pygame.K_DOWN :
					#direction = "up"
					lead_y_change = 0
			
			
		
		if lead_x >= display_width:		#direita
			tela = tela3#barreirana1
			lead_x = 0
		elif  lead_x < 0 :				#Esquerda
			tela = tela5#barreirana1
			lead_x = display_width
		elif lead_y >= display_height : #baixo
			tela = tela4 #barreirana1
			lead_y = 0
		elif lead_y < 0 :   			#cima
			tela = tela2
			lead_y = display_height
		lead_x += lead_x_change	
		lead_y += lead_y_change	
		
		gameDisplay.fill(black)	
		
		telas(tela)
	
		snakehead = []
		snakehead.append(lead_x)
		snakehead.append(lead_y)
		snakelist.append(snakehead)
		
		if len(snakelist)> snakeLenght:
			del snakelist[0]
		
			
		snake(snakelist,block_size)
		
		
		pygame.display.update()
		
				
		clock.tick(FPS)
		
	pygame.quit()
	quit()
	
game_intro()
gameLoop()