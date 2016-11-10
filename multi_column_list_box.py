import tkinter.font as tkFont
import tkinter.ttk as ttk

class MultiColumnListbox:
	root = None
	columns = None
	rows = []
	sorted_column = None
	sorted_descending = 0

	def __init__(self, root, columns):
		self.tree = None
		self.columns = columns
		self.sorted_column = columns[0]
		self.root = root
		self._setup_widgets()
		self._build_tree()

	def insert(self, item):
		self.tree.insert("", "end", values = item)
		self.sort_by(self.sorted_column, self.sorted_descending)

	def clear(self):
		self.tree.delete(*self.tree.get_children())

	def sort_by(self, column, descending):
		self.sorted_column = column
		self.sorted_descending = descending

		data = [ (self.tree.set(child, column), child) for child in self.tree.get_children() ]
		data.sort(reverse = descending)
		
		for i, v in enumerate(data):
			self.tree.move(v[1], "", i)

		self.tree.heading(column, command = lambda column = column: self.sort_by(column, int(not descending)))

	def _setup_widgets(self):
		container = ttk.Frame(self.root)
		container.pack(fill = "both", expand = True)
		self.tree = ttk.Treeview(columns = self.columns, show = "headings")
		self.tree.grid(column = 0, row = 0, sticky = "nsew", in_ = container)
		container.grid_columnconfigure(0, weight = 1)
		container.grid_rowconfigure(0, weight = 1)
		
	def _build_tree(self):
		for column in self.columns:
			self.tree.heading(column, text = column.title(), command = lambda column = column: self.sort_by(column, 0))
	
		for item in self.rows:
			self.tree.insert("", "end", values = item)

			for i, v in enumerate(item):
				column_width = tkFont.Font().measure(v)

				if self.tree.column(self.columns[i], width = None) < column_width:
					self.tree.column(self.columns[i], width = column_width)