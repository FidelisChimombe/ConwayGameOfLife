
#fidelis chimombe
#python: conway game of life
#objective: build a complete desktop app in python using MVC architecture


from Tkinter import *
import time 

from board import *
class ConwayGui:
	def __init__(self,board):

		"""
		used to instantiate the game of life
		"""
		self.root=Tk()
		self.board=board
		self.size=self.board.getSize()
		self.canvas=Canvas(self.root,width=500,height=500)
		self.factor=500.0/self.size
		self.board_tracker={} #chose to use a dictionary because it enables fast look ups
		for x in range(self.size):
			for y in range(self.size):
				if self.board.getBoard()[(x,y)].isAlive():
					self.board_tracker[(x,y)]=self.canvas.create_rectangle(x*self.factor,y*self.factor,(x+1)*self.factor,(y+1)*self.factor,fill="red")
				else:
					self.board_tracker[(x,y)]=self.canvas.create_rectangle(x*self.factor,y*self.factor,(x+1)*self.factor,(y+1)*self.factor,fill="green")

		
		self.draw()
		
	def done(self):

		mainloop()

	def getBoard(self):
		"""
		returns the board object
		"""
		return self.board

	def draw(self):

		"""
		draws the current configuration of the state of life in the ecosystem, at every period
		"""

		self.canvas.delete(ALL)
		#self.clear()
		for x in range(self.size):
			for y in range(self.size):
				x1=x*self.factor
				y1=y*self.factor

				x2=(x+1)*self.factor
				y2=(y+1)*self.factor
				if (self.board.getBoard()[(x,y)].isAlive()):
					self.canvas.create_rectangle(x1,y1,x2,y2,fill="red")
					
				else:
					self.canvas.create_rectangle(x1,y1,x2,y2,fill="green")
				
		self.root.update()

		self.canvas.pack()
		


	def update(self):
		"""
		draws the current state of the board on the gui or on the shell
		"""
	
		self.getBoard().interaction()
		self.draw()



	#this might be needed in the case that you don't want to use self.canvas.delete(ALL) to clear the canvas

	# def clear(self):
		
	# 	if len(self.board_tracker)>0:
	# 		for x in range(self.size):
	# 			for y in range(self.size):
	# 				self.board_tracker[(x,y)]=self.canvas.create_rectangle(x*self.factor,y*self.factor,(x+1)*self.factor,(y+1)*self.factor,fill="green")


gosper_glider_gun=[(1,5),(1,6),(2,5),(2,6),(11,5),(11,6),(11,7),(12,4),(12,8),(13,3),(14,3),(13,9),
(14,9),(15,6),(16,4),(17,5),(17,6),(17,7),(16,8),(21,3),(22,3),(21,4),(22,4),(21,5),(22,5),(23,2),
(23,6),(25,1),(25,6),(25,2),(25,7),(35,3),(36,3),(35,4),(36,4),(18,6)]
b=Board(50)
block=[(25,25),(25,26),(26,25),(26,26)]
b.initialize(gosper_glider_gun)

cg=ConwayGui(b)
#running the simulation
while True:
	#print cg.getBoard().getLive()
	cg.update()
	time.sleep(0.02)
	
cg.done()
