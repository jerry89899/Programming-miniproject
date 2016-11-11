from autofillgui import AutocompleteEntry
import tkinter as tk

from main import MainScreen
from search import SearchScreen
from page_stack import stack as page_stack

root = tk.Tk()

main = MainScreen(root)
main.show()

root.attributes("-fullscreen", True)

root.mainloop()