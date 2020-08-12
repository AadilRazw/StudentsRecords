#DataPage
def secondScreen():
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
	namecolor = colorPassive
	nameActive = False
	name = ""
	nameRect = pygame.Rect(350,100,100,32)
	optionRect = pygame.Rect(557,32,20,32)

	font = pygame.font.Font(None,32)
	captfont = pygame.font.Font(None,50)
	win = pygame.display.set_mode((WIDTH,HEIGHT))
	caption = pygame.display.set_caption("Mysql")

	#Functions
	def border(x,y,w,h):
		border1 = pygame.draw.rect(win, FONTC, (x, y, w, h), 0)
	def displayData():
		for i in range(1,len(datas)+1):
			put1 = str(datas[i-1][0])
			put2 = str(datas[i-1][1])
			put3 = str(datas[i-1][2])
			text1 = font.render(put1,True,FONTC)
			win.blit(text1,(100,200+i*32))
			text2 = font.render(put2,True,FONTC)
			win.blit(text2,(200,200+i*32))
			text3 = font.render(put3,True,FONTC)
			win.blit(text3,(350,200+i*32))
	mydb = mysql.connector.connect(host = "localhost",user = secrets.username,passwd = secrets.password)
	c = mydb.cursor()
	try:
		c.execute("CREATE DATABASE practise;")
		c.execute("USE practise;")
		c.execute("CREATE TABLE test(SID INTEGER PRIMARY KEY,Name VARCHAR(50),phoneNO INTEGER);")
	except:
		pass
	c.execute("use practise;")
	c.execute("select * from test order by Sid;")
	datas = c.fetchall()
	
	#Mainloop

	while run:
		win.fill(WINDOWC)
		border(0,0,600,1)
		border(15, 0, 2, 600)
		border(0, 15, 600, 2)
		border(585, 0, 2, 600)
		border(0, 585, 600, 2)


		capt = captfont.render("Your DataBase! ",True,FONTC)
		option = captfont.render(":",True,FONTC)
		win.blit(option,(560,30))
		win.blit(capt,(170,30))
		pygame.draw.rect(win,colorPassive,optionRect,2)
		details = font.render("S.id          Name             PhoneNumber",True,FONTC)
		win.blit(details,(100,150))
		search = font.render("Search for name: ",True,FONTC)
		win.blit(search,(100,100))
		pygame.draw.rect(win,namecolor,nameRect,2)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				if nameRect.collidepoint(event.pos):
					namecolor = colorActive
					nameActive = True
				elif optionRect.collidepoint(event.pos):
					from ThirdScreen import thirdscreen
					run = False
				else:
					namecolor = colorPassive
					nameActive = False
			if event.type == pygame.KEYDOWN:
				if nameActive:
					if event.key == pygame.K_BACKSPACE:
						name = name[:-1]
					elif event.key == pygame.K_DELETE:
						name = ""
					elif event.key == pygame.K_KP_ENTER:
						if name != "":
							c.execute(f"Select * from test where name like '%{name}%';")
							datas = c.fetchall()
						else:
							c.execute("select * from test order by Sid;")
							datas = c.fetchall()
					else:
						name += event.unicode

		displayData()

		nameText = font.render(name,True,FONTC)
		win.blit(nameText,(nameRect.x+5,nameRect.y+5))
		nameRect.w = max(100,nameText.get_width())
		pygame.display.update()
		sleep(3)
secondScreen()
