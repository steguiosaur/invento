from customtkinter import CTkFrame
from customwidget import CtmTreeView
from utils import settings

class DashboardTab(CTkFrame):
    def __init__(self, parent):
        CTkFrame.__init__(self, parent)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)

        # create frame for account settings
        self.displayUserFrame = CTkFrame(self)
        self.displayUserFrame.grid(row=0, column=0, rowspan=1, columnspan=1, padx=(10, 5), pady=(10, 5), sticky="nsew")

        # create frame for list accounts
        self.displayNumcCategoryFrame = CTkFrame(self)
        self.displayNumcCategoryFrame.grid(row=1, column=0, rowspan=1, columnspan=1, padx=(10, 5), pady=(5, 5), sticky="nsew")

        # create frame for list accounts
        self.displayNumProductsFrame = CTkFrame(self)
        self.displayNumProductsFrame.grid(row=2, column=0, rowspan=1, columnspan=1, padx=(10, 5), pady=(5, 5), sticky="nsew")

        # create frame for list accounts
        self.displayNumSalesFrame = CTkFrame(self)
        self.displayNumSalesFrame.grid(row=3, column=0, rowspan=1, columnspan=1, padx=(10, 5), pady=(5, 10), sticky="nsew")

        # create frame for list accounts
        self.displaySalesGraphFrame = CTkFrame(self)
        self.displaySalesGraphFrame.grid(row=0, column=1, rowspan=2, columnspan=3, padx=(5, 10), pady=(10, 5), sticky="nsew")

        # create frame for list accounts
        self.displayAddedProductTable = CtmTreeView(self, theme=settings.table_theme_read())
        self.displayAddedProductTable.grid(row=2, column=1, rowspan=2, columnspan=3, padx=(5, 10), pady=(5, 10), sticky="nsew")

        # create table
        self.treeviewTable = self.displayAddedProductTable.get_treeview()
        self.treeviewTable["show"] = "headings"
        self.treeviewTable["columns"] = (1, 2, 3)
        self.treeviewTable.column(1, width=100)
        self.treeviewTable.column(2, width=100)
        self.treeviewTable.column(3, width=100)
        self.treeviewTable.heading(1, text="Product")
        self.treeviewTable.heading(2, text="Date Modified")
        self.treeviewTable.heading(3, text="User")
