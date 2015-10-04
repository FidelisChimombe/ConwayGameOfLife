from Tkinter import *
import time 

from board import *
class ConwayGui:
	def __init__(self,board):
		self.root=Tk()
		self.board=board
		self.size=self.board.getSize()
		self.canvas=Canvas(self.root,width=self.size*10,height=self.size*10)
		self.draw()
		
	def done(self):
		mainloop()

	def getBoard(self):
		return self.board

	def draw(self):
		self.canvas.delete(ALL)
		for x in range(self.size):
			for y in range(self.size):
				x1=x*10
				y1=y*10

				x2=(x+1)*10
				y2=(y+1)*10
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
		


gosper_glider_gun=[(1,5),(1,6),(2,5),(2,6),(11,5),(11,6),(11,7),(12,4),(12,8),(13,3),(14,3),(13,9),
(14,9),(15,6),(16,4),(17,5),(17,6),(17,7),(16,8),(21,3),(22,3),(21,4),(22,4),(21,5),(22,5),(23,2),
(23,6),(25,1),(25,6),(25,2),(25,7),(35,3),(36,3),(35,4),(36,4),(18,6)]
b=Board(40)

b.initialize(gosper_glider_gun)

cg=ConwayGui(b)
#running the simulation
while True:
	print cg.getBoard().getLive()
	cg.update()
	time.sleep(0.2)
	
cg.done()
