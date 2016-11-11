import config

import tkinter as tk
from tkinter import messagebox

from multi_column_list_box import MultiColumnListBox
from station_selector import SelectorScreen

import nsapi.stations as stations
from nsapi.errorHandling import NSException

class SearchScreen():
	root = None
	returnScreen = None
	
	# Frames
	primaryFrame = None
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

		self.primaryFrame = tk.Frame(self.root)
		self.topFrame = tk.Frame(self.primaryFrame, background = "#FFD61E")
		self.resultsFrame = tk.Frame(self.primaryFrame, background = "#FFD61E")

		self.annuleerButton = tk.Button(self.topFrame, text = "Annuleer", height = 4, width = 24, background = "#3F47CC", foreground = "#FFFFFF", font = "bold", command = self.hide)
		self.buttonA = tk.Button(self.topFrame, text = "Dit station", height = 4, width = 24, background = "#3F47CC", foreground = "#FFFFFF", font = "bold", command = lambda: self.display_departures(config.default_station))
		self.buttonB = tk.Button(self.topFrame, text = "Ander station", height = 4, width = 24, background = "#3F47CC", foreground = "#FFFFFF", font = "bold", command = self.open_station_selector)

		self.multiColumnListBox = MultiColumnListBox(self.resultsFrame, ["Bestemming", "Spoor","Tijd"])	

	def open_station_selector(self):
		self._hide()
		SelectorScreen(self.root).show(self)

	def display_departures(self, station):
		self.multiColumnListBox.clear()

		if station == None:
			station = config.default_station

		try:
			for i in stations.getDepartures(station):
				self.multiColumnListBox.insert((i["Destination"], i["DeparturePlatform"], i["DepartureTime"]))
		except NSException as e:
			messagebox.showerror("Error", str(e))			

	def show(self, returnScreen = None, station = None):
		if returnScreen != None:
			self.returnScreen = returnScreen

		self.primaryFrame.pack(fill = tk.BOTH, expand = True)
		self.topFrame.pack(side = tk.TOP, fill = tk.BOTH)
		self.resultsFrame.pack(side = tk.TOP, fill = tk.BOTH, expand = True)
		
		self.annuleerButton.pack(pady = 20, padx = (20, 0), side = tk.LEFT)
		self.buttonA.pack(pady = 20, padx = (20, 0), side = tk.LEFT)
		self.buttonB.pack(pady = 20, padx = (20, 0), side = tk.LEFT)

		self.display_departures(station)

	def hide(self):
		self._hide()

		if self.returnScreen != None:
			self.returnScreen.show()

	def _hide(self):
		self.primaryFrame.pack_forget()