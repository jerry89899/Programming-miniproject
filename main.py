import tkinter as tk
from search import searchScreen

class mainScreen():
	root = None
	bottomFrame = None
	
	# Frames
	mainFrame = None
	
	# Buttons
	buttonA = None

	def __init__(self, root):
		self.root = root

		self.mainFrame = tk.Frame(self.root)
		self.topFrame = tk.Frame(self.mainFrame, background = "#FFD61E")

		self.bottomFrame = tk.Frame(self.mainFrame, background = "#FFD61E")

		self.buttonA = tk.Button(self.topFrame, text = "Actuele vertrektijden", height = 4, width = 24, background = "#3F47CC", foreground = "#FFFFFF", font = "bold", command = self.openSearch)

	def openSearch(self):
		self.hide()
		searchScreen(self.root).show(self)

	def show(self, returnScreen = None):
		self.returnScreen = returnScreen
		
		self.mainFrame.pack(fill = tk.BOTH, expand = True)
		self.topFrame.pack(side = tk.TOP, fill = tk.BOTH)
		
		self.bottomFrame.pack(side = tk.TOP, fill = tk.BOTH, expand = True)

		self.buttonA.pack(pady = 20, padx = (20, 0), side = tk.LEFT)

	def hide(self):
		self.mainFrame.pack_forget()

		if self.returnScreen != None:
			self.returnScreen.show()