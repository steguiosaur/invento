from customtkinter import CTkFrame, CTkScrollbar, CTkTabview, CTkLabel, CTkEntry, CTkButton, CTkOptionMenu
from Functionality import settings
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
        self.tableFrame.grid(row=0, column=0, rowspan=3, columnspan=4, padx=(10, 10), pady=(10, 5), sticky="nsew")

        # table style
        self.treeViewStyle = ttk.Style()
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

        # create product table
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

        # create scroll on table
        self.yScroll = CTkScrollbar(self.tableFrame, orientation="vertical")
        self.yScroll.configure(command=self.treeView.yview)
        self.yScroll.pack(side='right', fill='y', anchor="w")
        self.treeView.configure(yscrollcommand=self.yScroll.set)
        self.treeView.pack(side='right', fill='both', expand=True)

        # create frame for search items
        self.searchItemFrame = CTkFrame(self)
        self.searchItemFrame.grid(row=3, column=0, rowspan=1, columnspan=2, padx=(10, 5), pady=(5, 10), sticky="nsew")

        # create frame for updating items
        self.modifyItemTab = CTkTabview(self)
        self.modifyItemTab.grid(row=3, column=2, rowspan=1, columnspan=2, padx=(5, 10), pady=(0, 10), sticky="nsew")
        self.modifyItemTab.add("Modify")
        self.modifyItemTab.add("Category")
        self.modifyItemTab.add("Add")
        self.modifyItemTab.add("Remove")

        # modify tab grids
        self.modifyItemTab.tab("Modify").columnconfigure(0, weight=1)
        self.modifyItemTab.tab("Modify").rowconfigure(0, weight=1)

        self.modifyItemTab.tab("Category").columnconfigure(0, weight=1)
        self.modifyItemTab.tab("Category").rowconfigure(0, weight=1)

        self.modifyItemTab.tab("Add").columnconfigure(0, weight=1)
        self.modifyItemTab.tab("Add").rowconfigure(0, weight=1)

        self.modifyItemTab.tab("Remove").columnconfigure(0, weight=1)
        self.modifyItemTab.tab("Remove").rowconfigure(0, weight=1)

        # frames for modifyItemTab
        self.modifyItemModifyFrame = CTkFrame(self.modifyItemTab.tab("Modify"))
        self.modifyItemModifyFrame.grid(row=0, column=0, sticky="nsew")

        self.modifyItemCategoryFrame = CTkFrame(self.modifyItemTab.tab("Category"))
        self.modifyItemCategoryFrame.grid(row=0, column=0, sticky="nsew")

        self.modifyItemAddFrame = CTkFrame(self.modifyItemTab.tab("Add"))
        self.modifyItemAddFrame.grid(row=0, column=0, sticky="nsew")

        self.modifyItemRemoveFrame = CTkFrame(self.modifyItemTab.tab("Remove"))
        self.modifyItemRemoveFrame.grid(row=0, column=0, sticky="nsew")

        # modify tab grids
        self.modifyItemModifyFrame.rowconfigure(0, weight=1)
        self.modifyItemModifyFrame.rowconfigure(1, weight=1)
        self.modifyItemModifyFrame.rowconfigure(2, weight=1)
        self.modifyItemModifyFrame.rowconfigure(3, weight=1)
        self.modifyItemModifyFrame.rowconfigure(4, weight=1)
        self.modifyItemModifyFrame.rowconfigure(5, weight=1)
        self.modifyItemModifyFrame.columnconfigure(0, weight=1)
        self.modifyItemModifyFrame.columnconfigure(1, weight=1)
        self.modifyItemModifyFrame.columnconfigure(2, weight=1)
        self.modifyItemModifyFrame.columnconfigure(3, weight=1)
        self.modifyItemModifyFrame.columnconfigure(4, weight=1)
        
        # labels
        self.productNameLabel = CTkLabel(self.modifyItemModifyFrame, text="Product Name:") 
        self.categoryLabel = CTkLabel(self.modifyItemModifyFrame, text="Category:") 
        self.inStockLabel = CTkLabel(self.modifyItemModifyFrame, text="Current Stock:") 
        self.buyingPriceLabel = CTkLabel(self.modifyItemModifyFrame, text="Buying Price:") 
        self.sellingPriceLabel = CTkLabel(self.modifyItemModifyFrame, text="Selling Price:") 

        # modify frame label grids
        self.productNameLabel.grid(row=0, column=1, sticky="w")
        self.categoryLabel.grid(row=1, column=1, sticky="w")
        self.inStockLabel.grid(row=2, column=1, sticky="w")
        self.buyingPriceLabel.grid(row=3, column=1, sticky="w")
        self.sellingPriceLabel.grid(row=4, column=1, sticky="w")

        # entry widgets
        self.productNameEntry = CTkEntry(self.modifyItemModifyFrame)
        self.categoryEntry = CTkOptionMenu(self.modifyItemModifyFrame)
        self.inStockEntry = CTkEntry(self.modifyItemModifyFrame)
        self.buyingPriceEntry = CTkEntry(self.modifyItemModifyFrame)
        self.sellingPriceEntry = CTkEntry(self.modifyItemModifyFrame)

        # modify tab entry widgets grids
        self.productNameEntry.grid(row=0, column=3, sticky="ew")
        self.categoryEntry.grid(row=1, column=3, sticky="ew")
        self.inStockEntry.grid(row=2, column=3, sticky="ew")
        self.buyingPriceEntry.grid(row=3, column=3, sticky="ew")
        self.sellingPriceEntry.grid(row=4, column=3, sticky="ew")

        # modify tab discard button
        self.discardButton = CTkButton(self.modifyItemModifyFrame, text="Discard", fg_color="#FF0F2F", hover_color="#AF0F2F", command=self.modify_item_discard)
        self.discardButton.grid(row=5, column=3, sticky="ew")

        # modify tab save button
        self.saveButton = CTkButton(self.modifyItemModifyFrame, text="Save", command=self.modify_item_save)
        self.saveButton.grid(row=5, column=1, sticky="ew")


        # category tab grid
        self.modifyItemCategoryFrame.columnconfigure(0, weight=1)
        self.modifyItemCategoryFrame.columnconfigure(1, weight=1)
        self.modifyItemCategoryFrame.columnconfigure(2, weight=1)
        self.modifyItemCategoryFrame.columnconfigure(3, weight=1)
        self.modifyItemCategoryFrame.columnconfigure(4, weight=1)
        self.modifyItemCategoryFrame.rowconfigure(0, weight=1)
        self.modifyItemCategoryFrame.rowconfigure(1, weight=1)
        self.modifyItemCategoryFrame.rowconfigure(2, weight=1)
        self.modifyItemCategoryFrame.rowconfigure(3, weight=1)
        self.modifyItemCategoryFrame.rowconfigure(4, weight=1)


    def tableStyle(self):
        appearance = settings.table_theme_read()
        if appearance == "dark":
            self.treeView["style"] = "darkAppearance.Treeview"
        else:
            self.treeView["style"] = "lightAppearance.Treeview"

    def modify_item_discard(self):
        print("Discard changes")

    def modify_item_save(self):
        print("Save Item")

