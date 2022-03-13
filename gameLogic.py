import tkinter as tk

class RenderObject():
	def __init__(self):
		pass
	#draws the object on the canvas
	def draw(self,canvas):
		pass

class Entity(RenderObject):
	def __init__(self,x,y,col_dist=10000):
		self.x = x
		self.y = y
		self.col_dist = col_dist
		#tag the entity to be removed
		self.remove = False
	def distance_squared_to(self,entity):
		return (self.x-entity.x)**2+(self.y-entity.y)**2
	def collides(self,entity):
		dist = self.distance_squared_to(entity)  
		return dist <= self.col_dist or dist <= entity.col_dist
	def process(self):
		pass
	def input_event(self,inp):
		print(inp)
class Sprite(Entity):
	def __init__(self,img,x,y,colDist=5):
		super().__init__(x,y,colDist)
		self.img = img
		self.scale_x = 1
		self.scale_y = 1
	def draw(self,canvas):	
		canvas.create_image(0,0,image=self.img,anchor=tk.NW)
class Circle(Entity):
	def __init__(self,radius,x,y):
		super().__init__(x,y,radius*radius)
		self.radius = radius
	def draw(self,canvas):
		canvas.create_oval(self.x-self.radius,self.y-self.radius,self.x+self.radius,self.y+self.radius)

class Obsticle(Circle):
	def process(self):
		self.x -= 5
class Player(Circle):
	def __init__(self,radius,x,y,colDist=5):
		super().__init__(radius,x,y)
		self.jumping = False
		self.gravity = 1
		self.velocity = 0
		self.ground = 150
		self.jump_height = 20
	def process(self):
		self.velocity += self.gravity
		self.y += self.velocity
		if self.y >= self.ground:
			self.velocity = 0
			self.y = self.ground
			self.jumping = False
	def input_event(self,inp):
		if inp.char == ' ' and not self.jumping:
			self.velocity -= self.jump_height
			self.jumping = True

if __name__=='__main__':
	circle = Circle(10,0,0)
