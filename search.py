import tkinter as tk
from multi_column_list_box import MultiColumnListBox
from station_selector import SelectorScreen
from page_stack import stack as page_stack

import nsapi.stations as stations

class SearchScreen():
	root = None
	returnScreen = None
	
	# Frames
	primaryFrame = None
	controlFrame = None
	resultsFrame = None
	
	# Buttons
	annuleerButton = None
	anderStationButton = None
	ditStationButton = None

	def __init__(self, root):
		self.root = root

		self.primaryFrame = tk.Frame(self.root)
		self.controlFrame = tk.Frame(self.primaryFrame, background = "#FFD61E")
		self.resultsFrame = tk.Frame(self.primaryFrame, background = "#FFD61E")

		self.annuleerButton = tk.Button(self.controlFrame, text = "Annuleer", height = 4, width = 24, background = "#3F47CC", foreground = "#FFFFFF", font = "bold", command = self.hide)
		self.buttonA = tk.Button(self.controlFrame, text = "Ander station", height = 4, width = 24, background = "#3F47CC", foreground = "#FFFFFF", font = "bold", command = self.open_station_selector)

		self.multiColumnListBox = MultiColumnListBox(self.resultsFrame, ["Bestemming", "Spoor","Tijd"])	
		self.multiColumnListBox.clear()

		for i in stations.getDepartures("Utrecht Centraal"):
			self.multiColumnListBox.insert((i["Destination"], i["DeparturePlatform"], i["DepartureTime"]))

	def open_station_selector(self):
		self._hide()
		SelectorScreen(self.root).show(self)

	def show(self, returnScreen = None):
		if returnScreen != None:
			self.returnScreen = returnScreen

		self.primaryFrame.pack(fill = tk.BOTH, expand = True)
		self.controlFrame.pack(side = tk.TOP, fill = tk.BOTH)
		self.resultsFrame.pack(side = tk.TOP, fill = tk.BOTH, expand = True)
		
		self.annuleerButton.pack(pady = 20, padx = (20, 0), side = tk.LEFT)
		self.buttonA.pack(pady = 20, padx = (20, 0), side = tk.LEFT)

	def hide(self):
		self._hide()

		if self.returnScreen != None:
			self.returnScreen.show()

	def _hide(self):
		self.primaryFrame.pack_forget()