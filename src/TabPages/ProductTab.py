from Functionality import settings
from customtkinter import CTkFrame, CTkScrollbar
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

        # table style
        self.treeViewStyle = ttk.Style()
        #self.treeViewStyle.theme_use("alt")
        self.treeViewStyle.configure(
            "lightAppearance.Treeview",
            highlightthickness=0,
            bd=0,
            relief="flat",
            rowheight="20",
            borderwidth=0,
            background="#e1e1e1",
            foreground="#202020"
        )
        self.treeViewStyle.configure(
            "lightAppearance.Treeview.Heading",
            borderwidth=0,
            relief="flat",
            font=("Roboto", 9, "bold"),
            background="#b1b1b1",
            foreground="#202020"
        )
        self.treeViewStyle.configure(
            "darkAppearance.Treeview",
            highlightthickness=0,
            bd=0,
            rowheight="20",
            relief="flat",
            borderwidth=0,
            background="#282828",
            foreground="#d1d1d1"
        )
        self.treeViewStyle.configure(
            "darkAppearance.Treeview.Heading",
            borderwidth=1,
            relief="flat",
            font=("Roboto", 9, "bold"),
            background="#202020",
            foreground="#d1d1d1",

        )

        self.treeViewStyle.layout("lightAppearance.Treeview", [('lightAppearance.Treeview.treearea', {'sticky': 'nsew'})])
        self.treeViewStyle.layout("darkAppearance.Treeview", [('lightAppearance.Treeview.treearea', {'sticky': 'nsew'})])

        self.treeView = ttk.Treeview(self.tableFrame, selectmode='extended', height=100)
        self.tableStyle()

        self.treeView["show"] = "headings"
        self.treeView["columns"] = ("1", "2", "3","4","5","6")
        
        self.treeView.column("1", width=100)
        self.treeView.column("2", width=70)
        self.treeView.column("3", width=30)
        self.treeView.column("4", width=30)
        self.treeView.column("5", width=30)
        self.treeView.column("6", width=30)

        self.treeView.heading("1", text="Product Name")
        self.treeView.heading("2", text="Category")
        self.treeView.heading("3", text="In-Stock")
        self.treeView.heading("4", text="Buying Price")
        self.treeView.heading("5", text="Selling Price")
        self.treeView.heading("6", text="Date Modified")

        self.yScroll = CTkScrollbar(self.tableFrame, orientation="vertical")
        self.yScroll.configure(command=self.treeView.yview)
        self.yScroll.pack(side='right', fill='y', anchor="w")
        self.treeView.configure(yscrollcommand=self.yScroll.set)
        self.treeView.pack(side='right', fill='both', expand=True)

        # create frame for adding items
        self.modifyItemFrame = CTkFrame(self)
        self.modifyItemFrame.grid(row=3, column=0, rowspan=1, columnspan=2, padx=(10, 10), pady=(10, 10), sticky="nsew")

        # create frame for updating items
        self.updateItemFrame = CTkFrame(self)
        self.updateItemFrame.grid(row=3, column=2, rowspan=1, columnspan=2, padx=(10, 10), pady=(10, 10), sticky="nsew")

    def tableStyle(self):
        appearance = settings.table_theme_read()
        if appearance == "dark":
            self.treeView["style"] = "darkAppearance.Treeview"
        else:
            self.treeView["style"] = "lightAppearance.Treeview"
