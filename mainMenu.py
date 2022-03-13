import tkinter as tk
def show(f):
	
	FONT = ("Source Code Pro",20)
	main = tk.Tk()
	main.title("Python Dino GAME")	
	main.geometry("500x500")
	
	container = tk.Frame(main)
	container.pack(expand=True)	
	
	lbltitle = tk.Label(container,text="Welcome To Python Jumper",font=FONT)
	lbltitle.grid(row=0,column=0)
	
	inputFrame = tk.Frame(container)
	inputFrame.grid(row=1,column=0,pady=100)
	
	def onBtnPress():
		text = txtInput.get()
		container.destroy()
		#stop execution of the main loop	
		main.quit()
		f(main,text)	
	btnStart = tk.Button(inputFrame,text="Start Game",command=onBtnPress,font=FONT)
	btnStart.pack(side=tk.BOTTOM,pady=20)
	

	lblEntry = tk.Label(inputFrame,text="name: ",font=FONT)
	lblEntry.pack(side=tk.LEFT)	
	
	txtInput = tk.Entry(inputFrame,font=FONT)
	txtInput.pack(side=tk.RIGHT)
		
	main.mainloop()
if __name__ == '__main__':
	show("no")	
