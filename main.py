import tkinter as tk
from search import SearchScreen
from page_stack import stack as page_stack

class MainScreen():
	root = None
	returnScreen = None
	
	# Frames
	primaryFrame = None
	bottomFrame = None

	# Buttons
	buttonA = None

	def __init__(self, root):
		self.root = root
		
		self.primaryFrame = tk.Frame(self.root)
		self.topFrame = tk.Frame(self.primaryFrame, background = "#FFD61E")

		self.bottomFrame = tk.Frame(self.primaryFrame, background = "#FFD61E")

		self.buttonA = tk.Button(self.topFrame, text = "Actuele vertrektijden", height = 4, width = 24, background = "#3F47CC", foreground = "#FFFFFF", font = "bold", command = self.openSearch)

	def openSearch(self):
		self.hide()
		SearchScreen(self.root).show(self)

	def show(self, returnScreen = None):
		if returnScreen != None:
			self.returnScreen = returnScreen

		self.primaryFrame.pack(fill = tk.BOTH, expand = True)
		self.topFrame.pack(side = tk.TOP, fill = tk.BOTH)
		
		self.bottomFrame.pack(side = tk.TOP, fill = tk.BOTH, expand = True)

		self.buttonA.pack(pady = 20, padx = (20, 0), side = tk.LEFT)

	def hide(self):
		self._hide()

		if self.returnScreen != None:
			self.returnScreen.show()

	def _hide(self):
		self.primaryFrame.pack_forget()