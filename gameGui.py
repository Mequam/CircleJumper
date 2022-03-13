import tkinter as tk
import gameLogic as gl
from time import sleep
import random

#from PIL import Image, ImageTk

def buildGui(mainWindow,name):
	FONT = ("Source Code Pro",20)
	
	mainWindow.attributes("-fullscreen",True)
	
	guiCont = tk.Frame(mainWindow)
	guiCont.grid(row="0",column="0")

	lblName = tk.Label(guiCont,text="Name:",font=FONT)
	lblName.grid(row="0",column="0")

	lblNameDisp = tk.Label(guiCont,text=name,font=FONT)
	lblNameDisp.grid(row="0",column="1")

	lblHealth = tk.Label(guiCont,text="Hp:",font=FONT)
	lblHealth.grid(row="0",column="2",padx=20)
	
	lblHealthVal = tk.Label(guiCont,text="3",font=FONT)
	lblHealthVal.grid(row="0",column="3")
	
	canvas = tk.Canvas(mainWindow,height=500,width=500)
	canvas.grid(row="1",column="0")

	frameCount = 0	
	

	player = gl.Player(25,25,0)
	
	
	entities = [player]
	def pass_inp(inp):	
		for ent in entities:
			ent.input_event(inp)
	
	mainWindow.bind("<Key>",pass_inp)
	ground = mainWindow.winfo_height() / 2	
	
	player.ground = ground
	
	while True:
		canvas.delete('all')
		print(len(entities))
		for ent in entities:
			if ent.remove:
				entities.erase(ent)
			ent.draw(canvas)
				
			if ent != player:
				if ent.collides(player):
					print("game over")
					quit()
			ent.process()	
		if random.random() < 0.5/60:
			entities.append(gl.Obsticle(25,mainWindow.winfo_width(),ground))
		mainWindow.update_idletasks()
		mainWindow.update()
		frameCount += 1	
		sleep(1/60)
