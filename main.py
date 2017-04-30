import pygame
import time
import random

pygame.init()

white = (255,255,255)
black  = (0,0,0)
red = (255,0,0)

display_width = 800
display_height = 600

block_size = 10

FPS = 40

font = pygame.font.SysFont(None,25)
def snake (snakelist,block_size):
	for XnY in snakelist:
		pygame.draw.rect(gameDisplay, white,[XnY[0],XnY[1],block_size,block_size])

def message_to_screen (msg,color):
	screen_text = font.render(msg,True,color)
	gameDisplay.blit(screen_text,[display_width/2,display_height/2])
	
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("SNEK")
pygame.display.update()

clock = pygame.time.Clock()

def gameLoop():
	gameExit = False
	gameOver = False

	lead_x = display_width/2
	lead_y = display_height/2
	lead_x_change = 0
	lead_y_change = 0
	
	snakelist = []
	snakeLenght = 1
	
	randAppleX = round(random.randrange(0,display_width-block_size)/10.0)*10	
	randAppleY = round(random.randrange(0, display_height-block_size)/10.0)*10

	while not gameExit:
	
		while gameOver == True:
			gameDisplay.fill(black)
			message_to_screen("GAME OVER  C para continuar ou Q para sair",red)
			
			for event in pygame.event.get():
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
					lead_x_change = -block_size
					lead_y_change = 0
				if event.key == pygame.K_RIGHT:
					lead_x_change = block_size
					lead_y_change = 0
				if event.key == pygame.K_UP:
					lead_y_change = -block_size
					lead_x_change = 0
				if event.key == pygame.K_DOWN:
					lead_y_change = block_size
					lead_x_change = 0
			if event.type == pygame.KEYUP :
				if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
					lead_x_change == 0
		
		if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0 :
			gameOver = True
				
		lead_x += lead_x_change	
		lead_y += lead_y_change	
		
		gameDisplay.fill(black)	
		
		pygame.draw.rect(gameDisplay ,white, [randAppleX,randAppleY ,block_size,block_size])
		
		snakehead = []
		snakehead.append(lead_x)
		snakehead.append(lead_y)
		snakelist.append(snakehead)
		
		if len(snakelist)> snakeLenght:
			del snakelist[0]
		
		for segment in snakelist [:-1]:
			if segment == snakehead:
				gameOver = True
			
		snake(snakelist,block_size)
		
		pygame.display.update()
		
		if lead_x == randAppleX and lead_y == randAppleY :
			randAppleX = round(random.randrange(0,display_width-block_size)/10.0)*10	
			randAppleY = round(random.randrange(0, display_height-block_size)/10.0)*10
			
			snakeLenght += 1
			
		clock.tick(FPS)
		
	pygame.quit()
	quit()
	
gameLoop()