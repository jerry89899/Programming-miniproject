import tkinter as tk

from tkinter import *
import re
from allstations import all_stations as stations
from autofillgui import AutocompleteEntry

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

    def __init__(self, root):
        self.root = root

        self.primaryFrame = tk.Frame(self.root)
        self.filterFrame = tk.Frame(self.primaryFrame, background="#FFD61E")
        self.stationsFrame = tk.Frame(self.primaryFrame, background="#FFD61E")
        self.bottomFrame = tk.Frame(self.primaryFrame, background="#FFD61E")
        self.buttonA = tk.Button(self.filterFrame, text="Annuleer", height=4, width=24, background="#3F47CC", foreground="#FFFFFF", font="bold", command=self.hide)
        self.zoek = tk.Button(self.filterFrame, text="Zoek", height=4, width=24, background="#3F47CC", foreground="#FFFFFF", font="bold", command=self.doSearch)

        self.entry = AutocompleteEntry(extracted_stations, self.filterFrame, width = 100)

    def doSearch(self):
        self._hide()
        station = self.entry.var.get()
        self.returnScreen.show(None, station)

    def show(self, returnScreen=None):
        if returnScreen != None:
            self.returnScreen = returnScreen

        self.primaryFrame.pack(fill=tk.BOTH, expand=True)

        self.filterFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.entry.pack(side = tk.TOP, expand = True)

        self.stationsFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.bottomFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.buttonA.pack(pady=20, padx=(20, 0), side=tk.LEFT)
        self.zoek.pack(pady=20, padx=(20, 0), side=tk.LEFT)

    def hide(self):
        self._hide()

        if self.returnScreen != None:
            self.returnScreen.show()

    def _hide(self):
        self.primaryFrame.pack_forget()