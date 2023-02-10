from customtkinter import CTkFrame, CTkLabel
from customwidget import CtmTreeView, SalesGraph
from utils import accounts, itemdata, settings, Icon

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

        self.icons = Icon()
        # create frame for account settings
        self.displayUserFrame = CTkFrame(self)
        self.displayUserFrame.grid(row=0, column=0, rowspan=1, columnspan=1, padx=(10, 5), pady=(10, 5), sticky="nsew")
        self.displayUserFrame.grid_columnconfigure(0, weight=1)
        self.displayUserFrame.grid_columnconfigure(1, weight=1)
        self.displayUserFrame.grid_rowconfigure(0, weight=1)
        self.displayUserFrame.grid_rowconfigure(1, weight=0)
        self.displayUserFrame.grid_rowconfigure(2, weight=0)
        self.displayUserFrame.grid_rowconfigure(3, weight=1)
        self.displayUserFrame.grid_rowconfigure(4, weight=1)

        self.displayUserIconFrame = CTkFrame(self.displayUserFrame)
        self.displayUserIconFrame.grid(row=0, column=0, rowspan=5, columnspan=1, padx=(5, 0), pady=5, sticky="nsew")
        self.displayUserIconFrame.columnconfigure(0, weight=1)
        self.displayUserIconFrame.rowconfigure(0, weight=1)

        self.displayUserIcon = CTkLabel(self.displayUserIconFrame, image=self.icons.get_user(), text="")
        self.displayUserIcon.grid(row=0, column=0, sticky="nsew")

        self.userLabel = CTkLabel(self.displayUserFrame, text="TOTAL USERS", font=("Arial", 13, "bold"))
        self.userLabel.grid(row=1, column=1, sticky="ew")

        self.userNumLabel = CTkLabel(self.displayUserFrame, font=("Arial", 30, "bold"))
        self.current_users()
        self.userNumLabel.grid(row=3, column=1, sticky="ew")

        # create frame for list accounts
        self.displayNumCategoryFrame = CTkFrame(self)
        self.displayNumCategoryFrame.grid(row=1, column=0, rowspan=1, columnspan=1, padx=(10, 5), pady=(5, 5), sticky="nsew")
        self.displayNumCategoryFrame.grid_columnconfigure(0, weight=1)
        self.displayNumCategoryFrame.grid_columnconfigure(1, weight=1)
        self.displayNumCategoryFrame.grid_rowconfigure(0, weight=1)
        self.displayNumCategoryFrame.grid_rowconfigure(4, weight=1)

        self.displayNumProductsIconFrame = CTkFrame(self.displayNumCategoryFrame)
        self.displayNumProductsIconFrame.grid(row=0, column=0, rowspan=5, columnspan=1, padx=(5, 0), pady=5, sticky="nsew")
        self.displayNumProductsIconFrame.columnconfigure(0, weight=1)
        self.displayNumProductsIconFrame.rowconfigure(0, weight=1)

        self.displayNumProductsIcon = CTkLabel(self.displayNumProductsIconFrame, image=self.icons.get_categories(), text="")
        self.displayNumProductsIcon.grid(row=0, column=0, sticky="nsew")

        self.categoryLabel = CTkLabel(self.displayNumCategoryFrame, text=" CATEGORIES ", font=("Arial", 13, "bold"))
        self.categoryLabel.grid(row=1, column=1, sticky="ew")

        self.categoryNumLabel = CTkLabel(self.displayNumCategoryFrame, font=("Arial", 30, "bold"))
        self.current_category_num()
        self.categoryNumLabel.grid(row=3, column=1, sticky="ew")


        # create frame for list accounts
        self.displayNumProductsFrame = CTkFrame(self)
        self.displayNumProductsFrame.grid(row=2, column=0, rowspan=1, columnspan=1, padx=(10, 5), pady=(5, 5), sticky="nsew")
        self.displayNumProductsFrame.grid_columnconfigure(0, weight=1)
        self.displayNumProductsFrame.grid_columnconfigure(1, weight=1)
        self.displayNumProductsFrame.grid_rowconfigure(0, weight=1)
        self.displayNumProductsFrame.grid_rowconfigure(4, weight=1)

        self.displayNumProductsIconFrame = CTkFrame(self.displayNumProductsFrame)
        self.displayNumProductsIconFrame.grid(row=0, column=0, rowspan=5, columnspan=1, padx=(5, 0), pady=5, sticky="nsew")
        self.displayNumProductsIconFrame.columnconfigure(0, weight=1)
        self.displayNumProductsIconFrame.rowconfigure(0, weight=1)

        self.displayNumProductsIcon = CTkLabel(self.displayNumProductsIconFrame, image=self.icons.get_products(), text="")
        self.displayNumProductsIcon.grid(row=0, column=0, sticky="nsew")

        self.productLabel = CTkLabel(self.displayNumProductsFrame, text=" PRODUCTS ", font=("Arial", 13, "bold"))
        self.productLabel.grid(row=1, column=1, sticky="ew")

        self.productNumLabel = CTkLabel(self.displayNumProductsFrame, font=("Arial", 30, "bold"))
        self.current_product_num()
        self.productNumLabel.grid(row=3, column=1, sticky="ew")


        # create frame for list accounts
        self.displayNumSalesFrame = CTkFrame(self)
        self.displayNumSalesFrame.grid(row=3, column=0, rowspan=1, columnspan=1, padx=(10, 5), pady=(5, 10), sticky="nsew")
        self.displayNumSalesFrame.grid_columnconfigure(0, weight=1)
        self.displayNumSalesFrame.grid_columnconfigure(1, weight=1)
        self.displayNumSalesFrame.grid_rowconfigure(0, weight=1)
        self.displayNumSalesFrame.grid_rowconfigure(4, weight=1)

        self.displayNumSalesIconFrame = CTkFrame(self.displayNumSalesFrame)
        self.displayNumSalesIconFrame.grid(row=0, column=0, rowspan=5, columnspan=1, padx=(5, 0), pady=5, sticky="nsew")
        self.displayNumSalesIconFrame.columnconfigure(0, weight=1)
        self.displayNumSalesIconFrame.rowconfigure(0, weight=1)

        self.displayNumSalesIcon = CTkLabel(self.displayNumSalesIconFrame, image=self.icons.get_sales(), text="")
        self.displayNumSalesIcon.grid(row=0, column=0, sticky="nsew")

        self.salesLabel = CTkLabel(self.displayNumSalesFrame, text="TOTAL SOLD", font=("Arial", 13, "bold"))
        self.salesLabel.grid(row=1, column=1, sticky="ew")

        self.salesNumLabel = CTkLabel(self.displayNumSalesFrame, text="0", font=("Arial", 15, "bold"))
        self.current_earned_today()
        self.salesNumLabel.grid(row=3, column=1, sticky="ew")

        # create frame for list accounts
        self.displaySalesGraphFrame = SalesGraph(self)
        self.displaySalesGraphFrame.grid(row=0, column=1, rowspan=2, columnspan=3, padx=(5, 10), pady=(10, 5), sticky="nsew")

        # create frame modified products
        self.displayAddedProductFrame = CTkFrame(self)
        self.displayAddedProductFrame.grid(row=2, column=1, rowspan=2, columnspan=3, padx=(5, 10), pady=(5, 10), sticky="nsew")

        self.displayAddedProductFrame.grid_columnconfigure(0, weight=1)
        self.displayAddedProductFrame.grid_rowconfigure(0, weight=0)
        self.displayAddedProductFrame.grid_rowconfigure(1, weight=0)
        self.displayAddedProductFrame.grid_rowconfigure(2, weight=0)
        self.displayAddedProductFrame.grid_rowconfigure(3, weight=0)
        self.displayAddedProductFrame.grid_rowconfigure(4, weight=1)

        self.modifiedItemLabel = CTkLabel(self.displayAddedProductFrame, text="RECENT MODIFIED PRODUCTS", font=("Arial", 13, "bold"))
        self.modifiedItemLabel.grid(row=0, column=0, padx=(5, 0),  sticky="")

        self.displayAddedProductTable = CtmTreeView(self.displayAddedProductFrame, theme=settings.table_theme_read())
        self.displayAddedProductTable.grid(row=1, column=0, rowspan=4, sticky="nsew")

        # create table
        self.treeviewTable = self.displayAddedProductTable.get_treeview()
        self.treeviewTable["show"] = "headings"
        self.treeviewTable["columns"] = (1, 2, 3, 4)
        self.treeviewTable.column(1, width=100, anchor="center")
        self.treeviewTable.column(2, width=100, anchor="center")
        self.treeviewTable.column(3, width=50, anchor="center")
        self.treeviewTable.column(4, width=50, anchor="center")
        self.treeviewTable.heading(1, text="Product Name")
        self.treeviewTable.heading(2, text="Date Modified")
        self.treeviewTable.heading(3, text="Account")
        self.treeviewTable.heading(4, text="Permission")

        self.get_modifications()

    def get_modifications(self):
        self.treeviewTable.delete(*self.treeviewTable.get_children())
        for product in itemdata.view_modified():
            self.treeviewTable.insert("", "end", values=product)
            
    def refresh_graph(self):
        self.displaySalesGraphFrame.refresh_plot()

    def reload_treeview(self):
        self.displayAddedProductTable.change_theme(settings.table_theme_read())

    def current_users(self):
        self.userNumLabel.configure(text=str(accounts.count_non_admin_accounts()))

    def current_category_num(self):
        self.categoryNumLabel.configure(text=str(itemdata.count_category()))

    def current_product_num(self):
        self.productNumLabel.configure(text=str(itemdata.count_products()))

    def current_earned_today(self):
        self.salesNumLabel.configure(text=str(itemdata.get_today_sales()))

    def reload_all(self):
        self.reload_treeview()
        self.refresh_graph()
        self.get_modifications()
        self.current_users()
        self.current_category_num()
        self.current_product_num()
        self.current_earned_today()
