import tkinter as tk
<<<<<<< HEAD
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
=======
# from search import SearchScreen
from page_stack import stack as page_stack
from tkinter import *
import re
from allstations import all_stations as stations
from autofillgui import AutocompleteEntry as autocomplete

extracted_stations = []
for v in stations:
    extracted_stations.append(v["Names"]["Long"])
    if "Synonyms" in v:
        extracted_stations.extend(v["Synonyms"])


class SelectorScreen():
    root = None
    returnScreen = None

    # Frames
    primaryFrame = None
    filterFrame = None
    bottomFrame = None

    # Buttons
    buttonA = None
>>>>>>> refs/remotes/origin/master

    def __init__(self, root):
        self.root = root

<<<<<<< HEAD
		self.primaryFrame = tk.Frame(self.root)

		self.controlFrame = tk.Frame(self.primaryFrame, background = "#FFD61E")
		self.stationsFrame = tk.Frame(self.primaryFrame, background = "#FFD61E")

		self.buttonA = tk.Button(self.controlFrame, text = "Annuleer", height = 4, width = 24, background = "#3F47CC", foreground = "#FFFFFF", font = "bold", command = self.hide)
		self.buttonB = tk.Button(self.controlFrame, text = "Huidig station", height = 4, width = 24, background = "#3F47CC", foreground = "#FFFFFF", font = "bold")
=======
        self.primaryFrame = tk.Frame(self.root)
        self.filterFrame = tk.Frame(self.primaryFrame, background="#FFD61E")
        self.stationsFrame = tk.Frame(self.primaryFrame, background="#FFD61E")
        self.bottomFrame = tk.Frame(self.primaryFrame, background="#FFD61E")
        self.entry = tk.Entry(self.filterFrame, width=50, background="#3F47CC")
        self.buttonA = tk.Button(self.filterFrame, text="Annuleer", height=4, width=24, background="#3F47CC",
                                 foreground="#FFFFFF", font="bold", command=self.hide)

    def show(self, returnScreen=None):
        if returnScreen != None:
            self.returnScreen = returnScreen
>>>>>>> refs/remotes/origin/master

        self.primaryFrame.pack(fill=tk.BOTH, expand=True)

        self.filterFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

<<<<<<< HEAD
		self.controlFrame.pack(side = tk.TOP, fill = tk.BOTH)
		self.stationsFrame.pack(side = tk.TOP, fill = tk.BOTH, expand = True)
=======
        self.entry.pack(side=tk.TOP, expand=True)
        self.stationsFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.bottomFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.buttonA.pack(pady=20, padx=(20, 0), side=tk.LEFT)
>>>>>>> refs/remotes/origin/master

    def hide(self):
        self._hide()

        if self.returnScreen != None:
            self.returnScreen.show()

    def _hide(self):
        self.primaryFrame.pack_forget()

autocomplete(extracted_stations)
