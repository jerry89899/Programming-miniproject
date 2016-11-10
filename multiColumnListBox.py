import tkinter as tk
import tkinter.font as tkFont

class MultiColumnListbox(object):
	root = None

	def __init__(self, root):
		self.tree = None
		self._setup_widgets()
		self._build_tree()
		self.root = root

	def _setup_widgets(self):
		container = tk.Frame(self.root)
		container.pack(fill = tk.BOTH, expand=True)
		self.tree = tk.Treeview(columns=train_header, show="headings")
		self.tree.grid(column=0, row=0, sticky="nsew", in_=container)
		container.grid_columnconfigure(0, weight=1)
		container.grid_rowconfigure(0, weight=1)

	def _build_tree(self):
		for col in train_header:
			self.tree.heading(col, text=col.title(), command=lambda c=col: sortby(self.tree, c, 0))
			self.tree.column(col, width=tkFont.Font().measure(col.title()))

		for item in destination_list:
			self.tree.insert("", "end", values=item)
			
			for ix, val in enumerate(item):
				col_w = tkFont.Font().measure(val)
				if self.tree.column(train_header[ix],width=None)<col_w:
					self.tree.column(train_header[ix], width=col_w)

def sortby(tree, col, descending):
	data = [(tree.set(child, col), child) \
		for child in tree.get_children("")]
	data.sort(reverse=descending)
	for ix, item in enumerate(data):
		tree.move(item[1], "", ix)
	tree.heading(col, command=lambda col=col: sortby(tree, col, \
		int(not descending)))

train_header = ["Bestemming", "Spoor","Tijd"]
destination_list = [
("Zwoelle", "2","15:20") ,
("Zwolle", "2","15:20") ,
("Apeldoorn", "2","15:20") ,
("Zwolle", "2","15:20") ,
("Zwolle", "2","15:20") ,
("Zwolle", "2","15:20") ,
("Zwolle", "2","15:20") ,
("Zwolle", "2","15:20")
]


# if __name__ == "__main__":

#     root = tk.Tk()
#     root.attributes("-fullscreen", True)
#     root.title("nsapp")
#     listbox = MultiColumnListbox(root)
#     root.mainloop()
