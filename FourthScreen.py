#AddDataPage
def fourthscreen():
	import mysql.connector
	import pygame
	import secrets
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
	errorcolor = pygame.Color("red")
	idcolor = colorPassive
	namecolor = colorPassive
	phonecolor = colorPassive
	submitcolor = colorPassive
	backcolor = colorPassive
	nameActive = False
	idActive = False
	phoneActive = False
	submitActive = False
	helpText = False
	exist = False
	backActive = False
	idText = ""
	nameText = ""
	phoneText = ""
	digits = ["1","2","3","4","5","6","7","8","9","0"]
	idRect = pygame.Rect(100,250,32,32)
	nameRect = pygame.Rect(200,250,100,32)
	phoneRect = pygame.Rect(340,250,150,32)
	submitRect = pygame.Rect(230,320,150,50)
	backRect = pygame.Rect(500,30,70,32)
	font = pygame.font.Font(None,32)
	captfont = pygame.font.Font(None,50)
	win = pygame.display.set_mode((WIDTH,HEIGHT))
	caption = pygame.display.set_caption("Mysql")
	#Function
	def border(x,y,w,h):
		border1 = pygame.draw.rect(win, FONTC, (x, y, w, h), 0)
	def insert(x,y,z):
		try:
			data = (x,y,z)
			mydb = mysql.connector.connect(host = "localhost",user = secrets.username, passwd = secrets.password)
			c = mydb.cursor()
			c.execute("USE practise;")
			c.execute(f"Insert into test value{data}")
			mydb.commit()
			
			return False
		except:
			return True

	#Mainloop

	while run:
		win.fill(WINDOWC)
		border(0,0,600,1)
		border(15, 0, 2, 600)
		border(0, 15, 600, 2)
		border(585, 0, 2, 600)
		border(0, 585, 600, 2)
		addText = captfont.render("Add some people",True,FONTC)
		win.blit(addText,(170,100))
		details = font.render("S.id          Name             PhoneNumber",True,FONTC)
		win.blit(details,(100,200))
		pygame.draw.rect(win, idcolor, idRect, 2)
		pygame.draw.rect(win,namecolor,nameRect,2)
		pygame.draw.rect(win,phonecolor,phoneRect,2)
		pygame.draw.rect(win,submitcolor,submitRect)
		pygame.draw.rect(win,backcolor,backRect)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				if idRect.collidepoint(event.pos):
					idcolor = colorActive
					idActive = True
					nameActive = phoneActive = submitActive = backActive = False
					namecolor = phonecolor = submitcolor = backcolor = colorPassive
				elif nameRect.collidepoint(event.pos):
					namecolor = colorActive
					nameActive = True
					idActive = phoneActive = submitActive = backActive = False
					idcolor = phonecolor = submitcolor = backcolor = colorPassive
				elif phoneRect.collidepoint(event.pos):
					phonecolor = colorActive
					phoneActive = True
					nameActive = idActive = submitActive = backActive =  False
					namecolor = idcolor = submitcolor = backcolor = colorPassive
				elif submitRect.collidepoint(event.pos):
					submitcolor = colorActive
					submitActive = True
					if nameText != "" or idText != "" or phoneText != "":
						exist = insert(idText,nameText,phoneText)
						
						idText = nameText = phoneText = ""
						helpText = False
						
					else:
						helpText = True

					nameActive = idActive = phoneActive = backActive = False
					namecolor = idcolor = phonecolor = backcolor = colorPassive
				elif backRect.collidepoint(event.pos):
					backcolor = colorActive
					backActive = True
					nameActive = phoneActive = idActive = submitActive = False
					namecolor = phonecolor = idcolor = submitcolor = colorPassive
					from SecondScreen import secondScreen
					run = False
					
				else:
					idActive = nameActive = phoneActive = submitActive = backActive = False
					idcolor = namecolor = phonecolor = submitcolor = backcolor = colorPassive
			if idActive:
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_BACKSPACE:
						idText = idText[:-1]
					elif event.key == pygame.K_DELETE:
						idText = ""
					else:
						for i in digits:
							if event.unicode == i:
								idText += event.unicode
								break
			if nameActive:
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_BACKSPACE:
						nameText = nameText[:-1]
					elif event.key == pygame.K_DELETE:
						nameText = ""
					else:
						nameText += event.unicode
			if phoneActive:
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_BACKSPACE:
						phoneText = phoneText[:-1]
					elif event.key == pygame.K_DELETE:
						phoneText = ""
					else:
						for i in digits:
							if event.unicode == i:
								phoneText += event.unicode
								break

		if helpText:
			text = font.render("ENTER VALID DATA!!",True,FONTC)
			win.blit(text,(40,450))
		if exist:
			text = captfont.render("SID exist!! ",True,errorcolor)
			win.blit(text,(230,450))


		text1 = font.render(idText,True,FONTC)
		text2 = font.render(nameText,True,FONTC)
		text3 = font.render(phoneText,True,FONTC)
		text4 = captfont.render("Submit!",True,FONTC)
		text5 = font.render("Data!!",True,FONTC)

		win.blit(text1,(idRect.x+5,idRect.y+5))
		win.blit(text2,(nameRect.x+5,nameRect.y+5))
		win.blit(text3,(phoneRect.x+5,phoneRect.y+5))
		win.blit(text4,(submitRect.x+5,submitRect.y+5))
		win.blit(text5,(backRect.x+7,backRect.y+5))

		idRect.w = max(32,text1.get_width())
		nameRect.w = max(100,text2.get_width())
		phoneRect.w = max(150,text3.get_width())		
		pygame.display.update()
fourthscreen()