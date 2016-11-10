from autofillgui import AutocompleteEntry
import tkinter as tk

from main import mainScreen
from search import searchScreen

root = tk.Tk()

main = mainScreen(root)
main.show()

root.attributes("-fullscreen", True)

root.mainloop()