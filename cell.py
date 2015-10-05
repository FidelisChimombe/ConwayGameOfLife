
#fidelis chimombe
#python: conway game of life
#objective: build a complete desktop app in python using MVC architecture



from Tkinter import *
class Cell:

	def __init__(self, x, y, alive):
		"""
			this is the constructor of a cell, which represents a little square on the board
		"""
		self.x=x
		self.y=y
		self.alive=alive
		


	def getX(self):
		"""
			returns the x coordinate of a square
		"""
		return self.x



	def getY(self):
		"""
			returns the y coordinate of a square
		"""
		return self.y

	def isAlive(self):
		"""
			returns the current state of a cell, whether its alive or not
		"""
		return self.alive

	def cell_info(self):
		if(self.alive):
			print "( " + str(self.x) + " : " + str(self.y) + ") is alive"
		else:
			print "( " + str(self.x) + " : " + str(self.y) + ") is dead"
