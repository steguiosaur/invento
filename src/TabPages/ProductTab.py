from customtkinter import CTkFrame
from tkinter import ttk

class ProductTab(CTkFrame):
    def __init__(self, parent):
        CTkFrame.__init__(self, parent)

        # inventory tab grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=0)

        # create frame for table
        self.tableFrame = CTkFrame(self)
        self.tableFrame.grid(row=0, column=0, rowspan=3, columnspan=4, padx=(10, 10), pady=(10, 10), sticky="nsew")
        self.tableFrame.grid_columnconfigure(0, weight=1)
        self.tableFrame.rowconfigure(0, weight=1)

        # create table
        self.treeViewStyle = ttk.Style()
        self.treeViewStyle.theme_use("clam")
        self.treeViewStyle.configure(
            "Treeview",
            rowheight="20",
        )
        self.treeView = ttk.Treeview(self.tableFrame, selectmode='browse')
        self.treeView.grid(row=0, column=0, rowspan=1, columnspan=1,padx=(0,0), pady=(0,0), sticky="nsew")

        self.treeView["show"] = "headings"
        self.treeView["columns"] = ("1", "2", "3","4","5","6")
        
        self.treeView.column("1", width=100)
        self.treeView.column("2", width=40)
        self.treeView.column("3", width=5)
        self.treeView.column("4", width=5)
        self.treeView.column("5", width=5)
        self.treeView.column("6", width=5)

        self.treeView.heading("1", text="Product Name")
        self.treeView.heading("2", text="Category")
        self.treeView.heading("3", text="In-Stock")
        self.treeView.heading("4", text="Buying Price")
        self.treeView.heading("5", text="Selling Price")
        self.treeView.heading("6", text="Product Added")

        # create frame for adding items
        self.modifyItemFrame = CTkFrame(self)
        self.modifyItemFrame.grid(row=3, column=0, rowspan=1, columnspan=2, padx=(10, 10), pady=(10, 10), sticky="nsew")

        # create frame for updating items
        self.updateItemFrame = CTkFrame(self)
        self.updateItemFrame.grid(row=3, column=2, rowspan=1, columnspan=2, padx=(10, 10), pady=(10, 10), sticky="nsew")
