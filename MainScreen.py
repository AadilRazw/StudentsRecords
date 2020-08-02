#LoginPage
def mainscreen():
	import pygame
	from time import sleep
	pygame.init()
	#Variables
	WIDTH = 600
	HEIGHT = 600
	running = True
	WINDOWC = (255,255,255)
	FONTC = (0,0,0)
	colorActive = pygame.Color("lightskyblue3")
	colorPassive = pygame.Color("grey15")
	errorcolor = pygame.Color("red")
	usercolor = colorPassive
	passcolor = colorPassive
	submitcolor = colorPassive
	newcolor = colorPassive
	useractive = False
	passactive = False
	submitactive = False
	newActive = False
	helper = False
	error = False
	name = ""
	password = ""
	hidden = ""
	l = []

	passRect = pygame.Rect(250,230,140,32)
	userRect = pygame.Rect(250,170,140,32)
	submitrect = pygame.Rect(250,290,100,32)
	newrect = pygame.Rect(190,400,220,50)

	font = pygame.font.Font(None,32)
	captfont = pygame.font.Font(None,50)
	win = pygame.display.set_mode((WIDTH,HEIGHT))
	caption = pygame.display.set_caption("Mysql")

	#Functions
	def border(x,y,w,h):
		border1 = pygame.draw.rect(win, FONTC, (x, y, w, h), 0)

	#Mainloop
	while running:
		win.fill(WINDOWC)
		border(0,0,600,1)
		border(15, 0, 2, 600)
		border(0, 15, 600, 2)
		border(585, 0, 2, 600)
		border(0, 585, 600, 2)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				if userRect.collidepoint(event.pos):
					useractive = True
					passactive = submitactive = newActive = False
					usercolor = colorActive
					passcolor = submitcolor = newcolor = colorPassive
				elif passRect.collidepoint(event.pos):
					passactive = True
					useractive = submitactive = newActive = False
					passcolor = colorActive
					usercolor = submitcolor = newcolor = colorPassive
				elif submitrect.collidepoint(event.pos):
					useractive = passactive = newActive = False
					usercolor = passcolor = newcolor = colorPassive
					submitcolor = colorActive
					submitactive = True	
				elif newrect.collidepoint(event.pos):
					if name == "" and password == "":
						newcolor = colorActive
						newActive = True
						helper = True

						usercolor = passcolor = submitcolor = colorPassive
						useractive = passactive = submitactive = False
					else:
						newcolor = colorActive
						newActive = True
						usercolor = passcolor = submitcolor = colorPassive
						useractive = passactive = submitactive = False
						helper = False
						filename = (f"{name}.txt")
						f = open(filename,mode = "w")
						f.write(f"{name} \n{password}")
						f.close()
						name = password = hidden =  ""

				else:
					useractive =passactive= False
					usercolor =passcolor= colorPassive
			if useractive ==True:
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_BACKSPACE:
						name = name[:-1]
					elif event.key == pygame.K_DELETE:
						name = ""
					else:
						name += event.unicode
				error = False
				
			elif passactive == True:
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_BACKSPACE:
						password = password[:-1]
						hidden = len(password)*"*"
					elif event.key == pygame.K_DELETE:
						password = ""
						hidden = len(password)*"*"

					else:
						password += event.unicode
						hidden = len(password)*"*"
				error = False
			elif submitactive:
				try:
					if name!="" and password != "":
						filename = f"{name}.txt"
						f = open(filename,mode = "r")
						for i in f.readlines():
							data = i
							if "\n" in data:
								data = data[:-1]
							l.append(data)
					
						if name+" " == l[0] and password == l[1]:
							from SecondScreen import secondScreen
							#secondScreen()
							running = False
						
						else:
							name = password = hidden = ""
					else:
						name = password = hidden = ""
					error = False

				except:
					if name!="" and password != "":
						error = True
		if helper:
			helpText = captfont.render("Enter details!!",True,FONTC)
			win.blit(helpText,(190,500))
		if error:
			displayText = font.render("No such user found!!",True,errorcolor)
			win.blit(displayText,(190,490))
			name = password = hidden = ""



		pygame.draw.rect(win,usercolor,userRect,2)
		pygame.draw.rect(win,passcolor,passRect,2)
		pygame.draw.rect(win,submitcolor,submitrect)
		pygame.draw.rect(win,newcolor,newrect)




		finalname = font.render(name,True,FONTC)
		text1 = font.render("Username: ",True,FONTC)
		finalpassword = font.render(hidden,True,FONTC)
		text2 = font.render("Password: ",True,FONTC)
		text3 = font.render("Submit!",True,FONTC)
		newText = captfont.render("Create new!!",True,FONTC)
		win.blit(finalname,(userRect.x + 5,userRect.y + 5))
		win.blit(finalpassword,(passRect.x + 5,passRect.y + 5))
		win.blit(newText,(newrect.x+10,newrect.y+10))
		win.blit(text1,(130,175))
		win.blit(text2,(130,235))
		win.blit(text3,(255,295))
		



		userRect.w = max(100,finalname.get_width())
		passRect.w = max(100,finalpassword.get_width())

		pygame.display.update()
	sleep(2)
mainscreen()