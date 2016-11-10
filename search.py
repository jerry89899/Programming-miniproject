import tkinter as tk
from multiColumnListBox import MultiColumnListbox

class searchScreen():
	root = None
	returnScreen = None
	
	# Frames
	searchFrame = None
	topFrame = None
	resultsFrame = None
	entry = None

	# Entries
	entry = None
	
	# Buttons
	annuleerButton = None
	anderStationButton = None
	ditStationButton = None

	def __init__(self, root):
		self.root = root

		self.searchFrame = tk.Frame(self.root)
		self.topFrame = tk.Frame(self.searchFrame, background = "#FFD61E")
		self.resultsFrame = tk.Frame(self.searchFrame, background = "#FFD61E")

		self.annuleerButton = tk.Button(self.topFrame, text = "Annuleer", height = 4, width = 24, background = "#3F47CC", foreground = "#FFFFFF", font = "bold", command = self.hide)
		self.buttonA = tk.Button(self.topFrame, text = "Dit station", height = 4, width = 24, background = "#3F47CC", foreground = "#FFFFFF", font = "bold")
		self.buttonB = tk.Button(self.topFrame, text = "Ander station", height = 4, width = 24, background = "#3F47CC", foreground = "#FFFFFF", font = "bold")

		# self.entry = AutocompleteEntry([], self.topFrame, width = 1000)
		# self.entry.pack(side = tk.BOTTOM, pady = (0, 20), padx = (20, 20))
		
		self.entry = tk.Entry(self.topFrame, width=50)

		self.multiColumnListBox = MultiColumnListbox(self.resultsFrame)		
#		self.entry.pack(side = tk.BOTTOM, pady = (0, 20), padx = (20, 20))
	def show(self, returnScreen = None):
		self.returnScreen = returnScreen

		self.searchFrame.pack(fill = tk.BOTH, expand = True)
		self.topFrame.pack(side = tk.TOP, fill = tk.BOTH)
		self.resultsFrame.pack(side = tk.TOP, fill = tk.BOTH, expand = True)
		
		self.annuleerButton.pack(pady = 20, padx = (20, 0), side = tk.LEFT)
		self.buttonA.pack(pady = 20, padx = (20, 0), side = tk.LEFT)
		self.buttonB.pack(pady = 20, padx = (20, 0), side = tk.LEFT)
		self.entry.pack(side = tk.BOTTOM, pady = (0, 20), padx = (20, 20))

	def hide(self):
		self.searchFrame.pack_forget()
		self.topFrame.pack_forget()
		self.resultsFrame.pack_forget()

		self.annuleerButton.pack_forget()
		self.buttonA.pack_forget()
		self.buttonB.pack_forget()
		self.entry.pack_forget()

		if self.returnScreen != None:
			self.returnScreen.show()