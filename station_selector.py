import tkinter as tk
#from search import SearchScreen
from page_stack import stack as page_stack
from all_stations import all_stations as stations

class SelectorScreen():
	root = None
	returnScreen = None
	
	# Frames
	primaryFrame = None
	controlFrame = None
	bottomFrame = None
	
	# Buttons
	buttonA = None

	def __init__(self, root):
		self.root = root

		self.primaryFrame = tk.Frame(self.root)

		self.controlFrame = tk.Frame(self.primaryFrame, background = "#FFD61E")
		self.stationsFrame = tk.Frame(self.primaryFrame, background = "#FFD61E")

		self.buttonA = tk.Button(self.controlFrame, text = "Annuleer", height = 4, width = 24, background = "#3F47CC", foreground = "#FFFFFF", font = "bold", command = self.hide)
		self.buttonB = tk.Button(self.controlFrame, text = "Huidig station", height = 4, width = 24, background = "#3F47CC", foreground = "#FFFFFF", font = "bold")

	def show(self, returnScreen = None):
		if returnScreen != None:
			self.returnScreen = returnScreen

		self.primaryFrame.pack(fill = tk.BOTH, expand = True)

		self.controlFrame.pack(side = tk.TOP, fill = tk.BOTH)
		self.stationsFrame.pack(side = tk.TOP, fill = tk.BOTH, expand = True)

		self.buttonA.pack(pady = 20, padx = (20, 0), side = tk.LEFT)

	def hide(self):
		self._hide()

		if self.returnScreen != None:
			self.returnScreen.show()

	def _hide(self):
		self.primaryFrame.pack_forget()