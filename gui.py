
#fidelis chimombe
#python: conway game of life
#objective: build a complete desktop app in python using MVC architecture


from Tkinter import *
import time 
import threading

from board import *
class ConwayGui:
	def __init__(self,board):

		"""
		used to instantiate the game of life
		"""
		
		self.root=Tk()
		self.board=board
		self.size=self.board.getSize()
		self.factor=1000.0/self.size
		self.board_tracker={} #chose to use a dictionary because it enables fast look ups
		self.widgets()
		
		self.game_running=True
		self.delay=0.2


		self.gosper_glider_gun=[(1,5),(1,6),(2,5),(2,6),(11,5),(11,6),(11,7),(12,4),(12,8),(13,3),(14,3),(13,9),
		(14,9),(15,6),(16,4),(17,5),(17,6),(17,7),(16,8),(21,3),(22,3),(21,4),(22,4),(21,5),(22,5),(23,2),
		(23,6),(25,1),(25,6),(25,2),(25,7),(35,3),(36,3),(35,4),(36,4),(18,6)]

		self.block=[(25,15),(25,16),(26,15),(26,16)]
		self.current_configuration=self.gosper_glider_gun



		for x in range(self.size):
			for y in range(self.size):
				if self.board.getBoard()[(x,y)].isAlive():
					self.board_tracker[(x,y)]=self.canvas.create_oval(x*self.factor,y*self.factor,(x+1)*self.factor,(y+1)*self.factor,fill="red")
				else:
					self.board_tracker[(x,y)]=self.canvas.create_oval(x*self.factor,y*self.factor,(x+1)*self.factor,(y+1)*self.factor,fill="green")

		
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
					self.canvas.create_oval(x1,y1,x2,y2,fill="red")
					
				else:
					self.canvas.create_oval(x1,y1,x2,y2,fill="green")
				
		self.root.update()

	
		self.canvas.pack()

	
	def widgets(self):


		theLabel=Label(self.root,text="Welcome to the Conway Game of Life")
		theLabel.pack()


		#game life controls
		controlFrame=Frame(self.root)
		controlFrame.pack()
		pause=Button(controlFrame,text="pause",fg="green",command=self.pause)
		resume=Button(controlFrame,text="resume",fg="green",command=self.resume)
		slow_down=Button(controlFrame,text="slow down",fg="green",command=self.slow_down_button)
		speed_up=Button(controlFrame,text="Speed Up",fg="green",command=self.speed_up_button)
		pause.pack(side=LEFT)
		resume.pack(side=LEFT)
		slow_down.pack(side=LEFT)
		speed_up.pack(side=LEFT)
		





		


		#left display
		leftFrame=Frame(self.root)
		leftFrame.pack(side=LEFT)
		left_heading=Label(leftFrame,text="Game Configuration")
		left_heading.pack()
		b1=Button(leftFrame,text="gosper glider gun",fg="red",command=self.gosper)
		b2=Button(leftFrame,text="block",fg="blue",command=self.block)
		
		b1.pack()
		b2.pack()
		



		#middle display
		middleFrame=Frame(self.root)
		middleFrame.pack(side=LEFT)
		middle_heading=Label(middleFrame,text="The Game")
		middle_heading.pack()
		self.canvas=Canvas(middleFrame,width=1000,height=500,bg="yellow")

		#right display
		# rightFrame=Frame(self.root)
		# rightFrame.pack(side=LEFT)
		# right_heading=Label(rightFrame,text="Statistics")
		# right_heading.pack()
		# b4=Button(rightFrame,text="click me",fg="red")
		# b4.pack()


		


	def update(self):
		"""
		draws the current state of the board on the gui or on the shell
		"""
		if self.game_running:
			self.getBoard().interaction()
			self.draw()
		else:#on pause don't interact
			self.draw()
		

	def gosper(self):
		self.current_configuration=self.gosper_glider_gun
		self.board.initialize(self.current_configuration)

	

	def block(self):
		self.current_configuration=self.block
		self.board.initialize(self.current_configuration)
		



	def pause(self):
		#save the current state of the game
		current_board=dict(self.board.getBoard())
		self.board.board=current_board
		current_state=[]
		for x in range(self.size):
			for y in range(self.size):
				if self.board.getBoard()[(x,y)].isAlive():
					current_state.append((self.board.getBoard()[(x,y)].getX(),self.board.getBoard()[(x,y)].getY()))
		self.current_configuration=list(current_state)
		
		self.game_running=False
	

		


	def resume(self):
		self.game_running=True

	



	def stop(self):
		#grab the board current state and stop completely
		current_state=[]
		for x in range(self.size):
			for y in range(self.size):
				if self.board.getBoard()[(x,y)].isAlive():
					current_state.append((self.board.getBoard()[(x,y)].getX(),self.board.getBoard()[(x,y)].getY()))
		self.current_configuration=list(current_state)
		self.game_running=False
		print self.current_configuration
	


	def slow_down(self):
		while self.delay<1:
			self.delay+=0.2

	def slow_down_button(self):
		t=threading.Thread(target=self.slow_down,args=[])
		t.start()
		t.join()


	def speed_up(self):
		while self.delay>0.005:
			self.delay-=0.005


	def speed_up_button(self):
		t=threading.Thread(target=self.speed_up,args=[])
		t.start()
		t.join()



b=Board(50)
cg=ConwayGui(b)
cg.getBoard().initialize(cg.current_configuration)

#running the simulation:
while True:
	
	cg.update()

	time.sleep(cg.delay)
	
cg.done()
