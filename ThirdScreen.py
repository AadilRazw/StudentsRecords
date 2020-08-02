#OptionsPage
def thirdscreen():
	import mysql.connector
	import pygame
	pygame.init()
	from time import sleep
	#variables
	WIDTH = 600
	HEIGHT = 600
	run = True
	WINDOWC = (255,255,255)
	FONTC = (0,0,0)
	colorActive = pygame.Color("lightskyblue3")
	colorPassive = pygame.Color("grey15")
	delcolor = colorPassive
	addcolor = colorPassive
	namecolor = colorPassive
	nameActive = False
	delActive = False
	addActive = False
	name = ""
	delRect = pygame.Rect(205,190,200,50)
	addRect = pygame.Rect(205,260,200,50)

	font = pygame.font.Font(None,32)
	captfont = pygame.font.Font(None,50)
	win = pygame.display.set_mode((WIDTH,HEIGHT))
	caption = pygame.display.set_caption("Mysql")
	#Function
	def border(x,y,w,h):
		border1 = pygame.draw.rect(win, FONTC, (x, y, w, h), 0)
	def layout():
		delFont = captfont.render("Delete Data",True,FONTC)
		win.blit(delFont,(210,200))
		addFont = captfont.render("  Add Data",True,FONTC)
		win.blit(addFont,(210,270))
		pygame.draw.rect(win,delcolor,delRect,2)
		pygame.draw.rect(win,addcolor,addRect,2)
		pygame.display.update()


	#Mainloop

	while run:
		win.fill(WINDOWC)
		border(0,0,600,1)
		border(15, 0, 2, 600)
		border(0, 15, 600, 2)
		border(585, 0, 2, 600)
		border(0, 585, 600, 2)
		for event in pygame.event.get():
			if event.type ==pygame.QUIT:
				run = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				if addRect.collidepoint(event.pos):
					addcolor = colorActive
					addActive = True
					from FourthScreen import fourthscreen
				elif delRect.collidepoint(event.pos):
					delcolor = colorActive
					delActive = True
					from FifthScreen import fifthscreen
		if delActive == False and addActive == False:
			layout()
thirdscreen()