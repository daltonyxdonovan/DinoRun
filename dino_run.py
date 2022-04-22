import pygame, os, sys, time, random, shelve
from pygame.locals import *
from Dino import Dino
from cactus import Cactus
from cactusshort import CactusBaby

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("DINO RUN")

#colors
GREEN = (20, 255, 140)
GREY = (210, 210 ,210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
BLUE = (100, 100, 255)
BLACK = (0, 0, 0)
clock = pygame.time.Clock()
pygame.mixer.init(48000, -16, 1, 1024)
jump_sound = pygame.mixer.Sound("jump.wav")

#init stuff
pygame.mixer.pre_init(16000, 16, 2, 4096)
pygame.init()
myfont = pygame.font.SysFont("thick pixel", 25, bold=True)
myfont2 = pygame.font.SysFont("thick pixel", 12, bold=True)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
size = SCREEN_WIDTH, SCREEN_HEIGHT

#variables for the game
score = 0
counter = 0
vel = 10
v = 6
m = 4
onground = True
randomchoice = 1
gameovercounter = False
hicounter = 0


#objects and their locations
cactus1 = Cactus(RED, 30, 130, v)
cactus1.rect.x = 800
cactus1.rect.y = 525

cactusbaby = CactusBaby(WHITE, 120, 80, v)
cactusbaby.rect.x = 800
cactusbaby.rect.y = 585

playerDino = Dino(BLUE, 40, 70, 1, 15, True)
playerDino.rect.x = 300
playerDino.rect.y = 530

#setting groups and shit
incomingCacti = pygame.sprite.Group()
incomingCactibaby = pygame.sprite.Group()
player = pygame.sprite.Group()
player.add(playerDino)
incomingCacti.add(cactus1)
incomingCactibaby.add(cactusbaby)

#functions
def jumpnoise():
	pygame.mixer.Sound.play(jump_sound)

def playerimgdraw():
	playerimg = pygame.image.load('dino.png').convert_alpha()
	screen.blit(playerimg, ((playerDino.rect.x-50), (playerDino.rect.y-65)))
	
def cactus2imgdraw():
	cactusimg = pygame.image.load('cactus2.png').convert_alpha()
	screen.blit(cactusimg, ((cactus1.rect.x-50), (cactus1.rect.y-65)))
	
def cactusbabyimgdraw():
	cactus2img = pygame.image.load('cactusbaby.png').convert_alpha()
	screen.blit(cactus2img, ((cactusbaby.rect.x-40), (cactusbaby.rect.y-25)))
	
#main loop
running = True
game = False
titlerun = True
ticker = 0

def logoimg():
	logof = pygame.image.load("logo.png")
	screen.blit(logof, (x-60, 150))

def title():
	global titlerun
	global ticker
	global game
	
	screen.fill(BLACK)
	d = shelve.open('hiscore.txt')
	d['hiscore'] = hicounter
	d.close()
	startscore = myfont.render(str(hicounter), 0, (255,255,255))
	startscore_rect = startscore.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
	screen.blit(startscore, startscore.get_rect(topleft = screen.get_rect().topleft))
	startthing = myfont.render('dino run', 0, (255,255,255))
	startthing_rect = startthing.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
	screen.blit(startthing, startthing.get_rect(center = screen.get_rect().center))
	disclaimertext = myfont2.render("press enter to start", 5, (255,255,255))
	screen.blit(disclaimertext, (150, 480))
	pygame.display.flip()
	pygame.display.update()
	keys = pygame.key.get_pressed()
	while keys[pygame.K_RETURN]:
		d = shelve.open('hiscore.txt')
		d['hiscore'] = hicounter
		d.close()
		
		game = True
		titlerun = False
		return
	if keys[pygame.K_ESCAPE]:
		d = shelve.open('hiscore.txt')
		d['hiscore'] = hicounter
		d.close()
		exit()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			d = shelve.open('hiscore.txt')
			d['hiscore'] = hicounter
			d.close()
			exit()

#game function
def Game():
	global ticker
	global gameovercounter
	global score
	global hicounter
	global v
	global m
	global vel
	global randomchoice
	global onground
	global game
	score = score + 1
	screen.fill(WHITE)
	pygame.draw.rect(screen, BLACK, [0, 600, 800, 5], 0)
	playerDino.rect.y += (v)
	player.update()
	player.draw(screen)
	incomingCacti.update()
	incomingCacti.draw(screen)
	incomingCactibaby.update()
	incomingCactibaby.draw(screen)
	hiscoretext = myfont.render(str(hicounter), 10, (0,0,0))
	hiscoretext_rect = hiscoretext.get_rect(center=((SCREEN_WIDTH+20)/2, SCREEN_HEIGHT/2))
	screen.blit(hiscoretext, hiscoretext.get_rect(topleft = screen.get_rect().topleft))
	scoretext = myfont.render(str(score), False, (0,0,0))
	scoretext_rect = scoretext.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
	screen.blit(scoretext, scoretext.get_rect(topright = screen.get_rect().topright))

#which cactus spawns
	if randomchoice == 1:
		cactus2imgdraw()
		for Cactus in incomingCacti:
			Cactus.moveLeft(vel)
			while Cactus.rect.x < -50:
				Cactus.rect.x = 800
				vel = (vel + .5)
				print("\nYour velocity is now: " + str(vel))
				randomchoice = 2
	if randomchoice == 2:
		cactusbabyimgdraw()
		for CactusBaby in incomingCactibaby:
			CactusBaby.moveLeft(vel)
			while CactusBaby.rect.x < -150:
				CactusBaby.rect.x = 800
				vel = (vel + .5)
				print("\nYour velocity is now: " + str(vel))
				randomchoice = 1
	pygame.display.flip()
	pygame.display.update()
				
	#player floor and inputs
	keys = pygame.key.get_pressed()
	if playerDino.rect.y >= 530:
		playerDino.rect.y = 530
		onground = True
		v = 6
		m = 4
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit()
			
	#gravity mfer		
	if onground == True:
		if keys[pygame.K_SPACE]:
			jumpnoise()
			onground = False
	if onground == False:
		F =(1/2)*m*(v**2)
		playerDino.rect.y -= F
		v = v - .5
		if v < 0:
			m =-1
	if keys[pygame.K_ESCAPE]:
		quit()
	clock.tick(40)
	
#main game loop/ collision stuff
while running:
	while titlerun == True:
		title()
	while game == True:
		Game()
		sprite_collision_list = pygame.sprite.spritecollide(playerDino,incomingCacti,False)
		sprite_collision_list2 = pygame.sprite.spritecollide(playerDino,incomingCactibaby,False)
		for sprite in sprite_collision_list:
			gameoverpic = pygame.image.load('gameover.png').convert_alpha()
			screen.blit(gameoverpic, (195, 200))
			if score >= hicounter:
				hicounter = score
			d = shelve.open('hiscore.txt')
			d['hiscore'] = hicounter
			d.close()
			playerDino.rect.y = 530
			cactus1.rect.x = 800
			cactusbaby.rect.x=800
			counter = 0
			vel = 10
			score=0
			v = 6
			m = 4
			onground = True
			titlerun = True
			game = False
			pygame.display.flip()
			pygame.display.update()
			pygame.time.wait(3000)
		for sprite in sprite_collision_list2:
			gameoverpic = pygame.image.load('gameover.png').convert_alpha()
			screen.blit(gameoverpic, (195, 200))
			if score >= hicounter:
				hicounter = score
			d = shelve.open('hiscore.txt')
			d['hiscore'] = hicounter
			d.close()
			playerDino.rect.y = 530
			cactus1.rect.x = 800
			cactusbaby.rect.x=800
			counter = 0
			vel = 10
			score=0
			v = 6
			m = 4
			onground = True
			titlerun = True
			game = False
			pygame.display.flip()
			pygame.display.update()
			pygame.time.wait(3000)
