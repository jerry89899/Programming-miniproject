import tkinter as tk

from main import MainScreen
from search import SearchScreen

root = tk.Tk()

main = MainScreen(root)
main.show()

root.attributes("-fullscreen", True)

root.mainloop()