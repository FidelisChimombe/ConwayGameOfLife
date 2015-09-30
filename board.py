class Board:

	def __init__(self,width,height):
		"""
			this is the constructor for the board in the game of life
		"""
		self.width=width
		self.height=height
		self.board=[[]]
		for x in range(self.width):
			for y in range(self.height):
				self.board[x][y]=Cell(x,y,False);


	def getBoard(self):
		"""
			returns the current status of the board at any time
		"""
		return self.board


	def getCell(self,x,y):
		"""
			gets a cell from the board
		"""
		return self.board[x][y]

	def getLiveNeighbors(self,cell):
		"""
			counts the number of live cells neighboring a cell
		"""
		counter=0;
		x=cell.getX()
		y=cell.getY()

		if(getCell(x-1,y-1).isAlive()):
			counter++
		if(getCell(x,y-1).isAlive()):
			counter++
		if(getCell(x+1,y-1).isAlive()):
			counter++
		if(getCell(x-1,y).isAlive()):
			counter++
		if(getCell(x+1,y).isAlive()):
			counter++
		if(getCell(x-1,y+1).isAlive()):
			counter++
		if(getCell(x,y+1).isAlive()):
			counter++
		if(getCell(x+1,y+1).isAlive()):
			counter++
		return counter;

	def interaction(self):
		"""
			this represents one cycle of time in which a cell interacts with its neighbors
		"""

		for x in range(self.width):
			for y in range(self.height):
				#less than 2 neighbors die due to under population
				if(self.getLiveNeighbors(self.board[x][y])<2):
					self.board[x][y]=Cell(x,y,False)
				#more than 3 neighbors, over population, no resources, death
				elif self.getLiveNeighbors(self.board[x][y])>3:
					self.board[x][y]=Cell(x,y,False)
				#balanced population, supported economy, just right
				elif  2<=self.getLiveNeighbors(self.board[x][y])<=3:
					self.board[x][y]=Cell(x,y,True)
				#please resuurect, three angels have visited you
				elif  self.getLiveNeighbors(self.board[x][y])==3 and !self.board[x][y].isAlive():
					self.board[x][y]=Cell(x,y,True)

	def draw(self):
		"""draws the current state of the board on the gui or on the shell
		"""




