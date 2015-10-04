from cell import Cell
class Board:

	def __init__(self,size):
		"""
			this is the constructor for the board in the game of life
		"""
		self.size=size
		
		self.board={}

		#use dictionary to represent the board
		for x in range(self.size):
			for y in range(self.size):
				self.board[(x,y)]=Cell(x,y,False)
	

	def getSize(self):
		return self.size

	def getLive(self):
		"""
		returns the number of live cells in the board
		"""
		live_ones=0
		for i in range(self.size):
			for j in range(self.size):
				if self.getCell(i,j).isAlive():
					live_ones+=1
				else:
					continue
		return live_ones
	def getBoard(self):
		"""
			returns the current status of the board at any time
		"""
		return self.board


	def getCell(self,x,y):
		"""
			gets a cell from the board
		"""
		return self.board[(x,y)]

	def getLiveNeighbors(self,cell):
		"""
			counts the number of live cells neighboring a cell
		"""
		counter=0;
		x=cell.getX()
		y=cell.getY()
		for i in range(-1,2,1):
			for j in range(-1,2,1):
				if i==0 and j==0:
					pass
				elif(x+i<0 or x+i>=self.size or y+j<0 or y+j>=self.size):
					pass
				else:
					cell=self.getCell(x+i,y+j).isAlive()
					if(cell):
						counter+=1

		return counter

	def interaction(self):
		"""
			this represents one cycle of time in which a cell interacts with its neighbors
		"""
		temp_board=dict(self.getBoard())
		#self.clear()
		for x in range(self.size):
			for y in range(self.size):
				#less than 2 neighbors die due to under population
				if(self.getLiveNeighbors(temp_board[(x,y)])<2):
					temp_board[(x,y)]=Cell(x,y,False)
				#more than 3 neighbors, over population, no resources, death
				elif self.getLiveNeighbors(temp_board[(x,y)])>3:
					temp_board[(x,y)]=Cell(x,y,False)
				#balanced population, supported economy, just right
				elif  2<=self.getLiveNeighbors(temp_board[(x,y)])<=3:
					temp_board[(x,y)]=Cell(x,y,True)
				#please resuurect, three angels have visited you
				elif  self.getLiveNeighbors(temp_board[(x,y)])==3 and not temp_board[(x,y)].isAlive():
					temp_board[(x,y)]=Cell(x,y,True)
				else:
					pass
		self.board=dict(temp_board)

	


	def initialize(self,config):
		"""
			config is a list of tuples containing a configuration to be loaded
			sets the board with a new configuration
		"""
		self.clear()
		#make sure to call clear before initializing a configuration
		temp_board=dict(self.getBoard())
		for i in config:
			temp_board[(i[0],i[1])]=Cell(i[0],i[1],True)
		self.board=dict(temp_board)

	def insert(self,x,y,status):
		"""
		x, is the x coordinate of a cell
		y, is the y coordinate of a cell
		status, tells whether cell is alive or not
		"""
		self.board[(x,y)]=Cell(x,y,status)

	def clear(self):
		"""
		clears the board, before redrawing the configuration, before changing configuration
		"""
		temp_board=dict(self.getBoard())
		for x in range(self.getSize()):
			for y in range(self.getSize()):
				temp_board[(x,y)]=Cell(x,y,False)
		self.board=dict(temp_board)
		






