#DelDataPage
def fifthscreen():
	import pygame
	import mysql.connector
	from time import sleep
	pygame.init()

	#Variables
	WIDTH = 600
	HEIGHT = 600
	run = True
	WINDOWC = (255,255,255)
	FONTC = (0,0,0)
	colorActive = pygame.Color("lightskyblue3")
	colorPassive = pygame.Color("grey15")
	errorcolor = pygame.Color("red")
	usercolor = colorPassive
	submitcolor = colorPassive
	backcolor = colorPassive
	userRect = pygame.Rect(250,170,200,50)
	submitrect = pygame.Rect(190,290,200,50)
	backRect = pygame.Rect(500,30,70,32)
	userActive = False
	submitActive = False
	notvalid = False
	backActive = False
	name = ""
	
	font = pygame.font.Font(None,32)
	captfont = pygame.font.Font(None,50)
	win = pygame.display.set_mode((WIDTH,HEIGHT))
	caption = pygame.display.set_caption("Mysql")


	#Functions
	def border(x,y,w,h):
		border1 = pygame.draw.rect(win, FONTC, (x, y, w, h), 0)
	def delete(x):
		try:
			mydb = mysql.connector.connect(host = "localhost", user = "root",passwd = "root")
			c = mydb.cursor()
			c.execute("USE practise;")
			c.execute(f"delete from test where name = '{x}';")
			mydb.commit()
			return True
		except:
			return False

	#Mainloop

	while run:
		win.fill(WINDOWC)
		border(0,0,600,1)
		border(15, 0, 2, 600)
		border(0, 15, 600, 2)
		border(585, 0, 2, 600)
		border(0, 585, 600, 2)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			if event.type == pygame.MOUSEBUTTONDOWN:
				if userRect.collidepoint(event.pos):
					userActive = True
					usercolor = colorActive
					submitActive = backActive = False
					submitcolor = backcolor = colorPassive
				elif submitrect.collidepoint(event.pos):
					submitActive = True
					submitcolor = colorActive
					userActive = backActive = False
					usercolor = backcolor = colorPassive
					output = delete(name)
					name = ""
					if output == False:
						notvalid = True
					else:
						notvalid = False
				elif backRect.collidepoint(event.pos):
					backActive = True
					backcolor = colorActive
					userActive = submitActive = False
					usercolor = submitcolor = colorPassive
					from SecondScreen import secondScreen
					run = False
				else:
					submitActive = userActive = False
					usercolor = submitcolor = colorPassive
			if userActive:
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_BACKSPACE:
						name = name[:-1]
					elif event.key == pygame.K_DELETE:
						name = ""
					else:
						name += event.unicode


		if notvalid:
			text = captfont.render("Enter Valid name!!",True,errorcolor)
			win.blit(text,(150,400))

		pygame.draw.rect(win,usercolor,userRect,2)
		pygame.draw.rect(win,submitcolor,submitrect)
		pygame.draw.rect(win,backcolor,backRect)

		subText = captfont.render("Submit!",True,FONTC)
		win.blit(subText,(submitrect.x+20,submitrect.y+10))
		details = captfont.render("Enter name to delete!! ",True,FONTC)
		nameText = captfont.render("Name: ",True,FONTC)
		text = font.render("Data!!",True,FONTC)
		win.blit(nameText,(100,180))
		win.blit(details,(100,70))
		win.blit(text,(backRect.x+7,backRect.y+5))


		show = captfont.render(name,True,FONTC)
		win.blit(show,(userRect.x+10,userRect.y+10))


		pygame.display.update()

fifthscreen()


