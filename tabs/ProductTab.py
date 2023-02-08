from customtkinter import CTkFrame, CTkTabview, CTkLabel, CTkEntry, CTkButton, CTkOptionMenu
from customwidget import IntSpinbox, CtmTreeView
from utils import settings, itemdata, Icon

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

        #----------------------- TABLE FRAME -----------------------
        self.ascending = True
        self.table = CtmTreeView(self, theme=settings.table_theme_read())
        self.table.grid(row=0, column=0, rowspan=3, columnspan=4, padx=(10, 10), pady=(10, 5), sticky="nsew")
        # create product table
        self.treeView = self.table.get_treeview()
        self.treeView["show"] = "headings"
        self.treeView["columns"] = ("1", "2", "3", "4", "5", "6")
        self.treeView.column("1", width=180, anchor="center")
        self.treeView.column("2", width=70, anchor="center")
        self.treeView.column("3", width=20, anchor="center")
        self.treeView.column("4", width=40, anchor="center")
        self.treeView.column("5", width=40, anchor="center")
        self.treeView.column("6", width=100, anchor="center")
        self.treeView.heading("1", text="Product Name", command=lambda: self.sort_by_column("item"))
        self.treeView.heading("2", text="Category", command=lambda: self.sort_by_column("category"))
        self.treeView.heading("3", text="In-Stock", command=lambda: self.sort_by_column("in_stock"))
        self.treeView.heading("4", text="Buying Price", command=lambda: self.sort_by_column("buying_price"))
        self.treeView.heading("5", text="Selling Price", command=lambda: self.sort_by_column("selling_price"))
        self.treeView.heading("6", text="Date Modified", command=lambda: self.sort_by_column("date_modified"))

        self.get_all_inventory()

        #----------------------- SEARCH FRAME -----------------------
        self.searchItemFrame = CTkFrame(self)
        self.searchItemFrame.grid(row=3, column=0, rowspan=1, columnspan=2, padx=(10, 5), pady=(5, 10), sticky="nsew")
        self.searchItemFrame.grid_columnconfigure(0, weight=1)
        self.searchItemFrame.grid_columnconfigure(1, weight=1)
        self.searchItemFrame.grid_columnconfigure(2, weight=1)
        self.searchItemFrame.grid_columnconfigure(3, weight=0)
        self.searchItemFrame.grid_columnconfigure(4, weight=1)
        self.searchItemFrame.grid_rowconfigure(0, weight=0)
        self.searchItemFrame.grid_rowconfigure(1, weight=0)
        self.searchItemFrame.grid_rowconfigure(2, weight=1)
        self.searchItemFrame.grid_rowconfigure(3, weight=1)

        # search item entry
        self.searchItemEntry = CTkEntry(self.searchItemFrame, placeholder_text="Search Item")
        self.searchItemEntry.grid(row=0, column=0, columnspan=4, padx=(10, 5), pady=(10, 5), sticky="ew")

        self.icons = Icon()
        self.searchItemButton = CTkButton(self.searchItemFrame, image=self.icons.get_search(), text="Search", command=lambda: self.search())
        self.searchItemButton.grid(row=0, column=4, padx=(0, 5), pady=(10, 5), sticky="")

        # status frame
        self.statusReplyLabel = CTkLabel(self.searchItemFrame, text="")
        self.statusReplyLabel.grid(row=1, column=0, columnspan=5)

        #----------------------- ADD SALES FRAME -----------------------
        self.salesFrame = CTkFrame(self.searchItemFrame)
        self.salesFrame.grid(row=2, column=0, columnspan=5, rowspan=3, padx=(10, 10), pady=(5, 10), sticky="nsew")
        self.salesFrame.grid_columnconfigure(0, weight=1)
        self.salesFrame.grid_columnconfigure(1, weight=1)
        self.salesFrame.grid_columnconfigure(2, weight=1)
        self.salesFrame.grid_columnconfigure(3, weight=1)
        self.salesFrame.grid_columnconfigure(4, weight=1)
        self.salesFrame.grid_rowconfigure(0, weight=0)
        self.salesFrame.grid_rowconfigure(1, weight=1)
        self.salesFrame.grid_rowconfigure(2, weight=1)
        self.salesFrame.grid_rowconfigure(3, weight=1)
        self.salesFrame.grid_rowconfigure(4, weight=1)
        self.salesFrame.grid_rowconfigure(5, weight=1)

        self.currentSalesLabel = CTkLabel(self.salesFrame, text="CURRENT PRODUCT SALES", font=("Arial", 13, "bold"))
        self.currentSalesLabel.grid(row=0, column=0, columnspan=5, sticky="ew")

        self.salesLabel = CTkLabel(self.salesFrame, text="Add Sales")
        self.salesLabel.grid(row=1, column=1)

        self.salesSpinBox = IntSpinbox(self.salesFrame, min_value=0, max_value=100, step_size=1)
        self.salesSpinBox.grid(row=2, column=1, sticky="ew")

        self.salesButton = CTkButton(self.salesFrame, text="Add", command=lambda: print("save sales"))
        self.salesButton.grid(row=3, column=1, sticky="ew")

        self.removeSalesLabel = CTkLabel(self.salesFrame, text="Remove Sales")
        self.removeSalesLabel.grid(row=1, column=3)

        self.removeSalesSpinBox = IntSpinbox(self.salesFrame, min_value=0, step_size=1)
        self.removeSalesSpinBox.grid(row=2, column=3, sticky="ew")

        self.removeSalesButton = CTkButton(self.salesFrame, text="Remove", fg_color="#FF0F2F", hover_color="#AF0F2F", command=lambda: print("remove sales"))
        self.removeSalesButton.grid(row=3, column=3, sticky="ew")

        #----------------------- TAB CREATE FRAME -----------------------
        self.modifyItemTab = CTkTabview(self, command=lambda: print("action"))
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
        self.modifyItemModifyFrame.rowconfigure(0, weight=1)
        self.modifyItemModifyFrame.rowconfigure(1, weight=1)
        self.modifyItemModifyFrame.rowconfigure(2, weight=1)
        self.modifyItemModifyFrame.rowconfigure(3, weight=1)
        self.modifyItemModifyFrame.rowconfigure(4, weight=1)
        self.modifyItemModifyFrame.rowconfigure(5, weight=1)
        self.modifyItemModifyFrame.rowconfigure(6, weight=1)
        self.modifyItemModifyFrame.rowconfigure(7, weight=1)
        self.modifyItemModifyFrame.columnconfigure(0, weight=1)
        self.modifyItemModifyFrame.columnconfigure(1, weight=1)
        self.modifyItemModifyFrame.columnconfigure(2, weight=1)
        self.modifyItemModifyFrame.columnconfigure(3, weight=1)
        self.modifyItemModifyFrame.columnconfigure(4, weight=1)

        self.modifyItemCategoryFrame = CTkFrame(self.modifyItemTab.tab("Category"))
        self.modifyItemCategoryFrame.grid(row=0, column=0, sticky="nsew")
        self.modifyItemCategoryFrame.columnconfigure(0, weight=1)
        self.modifyItemCategoryFrame.columnconfigure(1, weight=1)
        self.modifyItemCategoryFrame.columnconfigure(2, weight=1)
        self.modifyItemCategoryFrame.columnconfigure(3, weight=1)
        self.modifyItemCategoryFrame.columnconfigure(4, weight=1)
        self.modifyItemCategoryFrame.rowconfigure(0, weight=1)
        self.modifyItemCategoryFrame.rowconfigure(1, weight=0)
        self.modifyItemCategoryFrame.rowconfigure(2, weight=0)
        self.modifyItemCategoryFrame.rowconfigure(3, weight=1)
        self.modifyItemCategoryFrame.rowconfigure(4, weight=0)
        self.modifyItemCategoryFrame.rowconfigure(5, weight=0)
        self.modifyItemCategoryFrame.rowconfigure(6, weight=1)

        self.modifyItemAddFrame = CTkFrame(self.modifyItemTab.tab("Add"))
        self.modifyItemAddFrame.grid(row=0, column=0, sticky="nsew")
        self.modifyItemAddFrame.rowconfigure(0, weight=1)
        self.modifyItemAddFrame.rowconfigure(1, weight=1)
        self.modifyItemAddFrame.rowconfigure(2, weight=1)
        self.modifyItemAddFrame.rowconfigure(3, weight=1)
        self.modifyItemAddFrame.rowconfigure(4, weight=1)
        self.modifyItemAddFrame.rowconfigure(5, weight=1)
        self.modifyItemAddFrame.rowconfigure(6, weight=1)
        self.modifyItemAddFrame.rowconfigure(7, weight=1)
        self.modifyItemAddFrame.columnconfigure(0, weight=1)
        self.modifyItemAddFrame.columnconfigure(1, weight=1)
        self.modifyItemAddFrame.columnconfigure(2, weight=1)
        self.modifyItemAddFrame.columnconfigure(3, weight=1)
        self.modifyItemAddFrame.columnconfigure(4, weight=1)

        self.modifyItemRemoveFrame = CTkFrame(self.modifyItemTab.tab("Remove"))
        self.modifyItemRemoveFrame.grid(row=0, column=0, sticky="nsew")
        self.modifyItemRemoveFrame.grid_columnconfigure(0, weight=1)
        self.modifyItemRemoveFrame.grid_columnconfigure(1, weight=1)
        self.modifyItemRemoveFrame.grid_columnconfigure(2, weight=1)
        self.modifyItemRemoveFrame.grid_rowconfigure(0, weight=1)
        self.modifyItemRemoveFrame.grid_rowconfigure(1, weight=1)
        self.modifyItemRemoveFrame.grid_rowconfigure(2, weight=0)
        self.modifyItemRemoveFrame.grid_rowconfigure(3, weight=0)
        self.modifyItemRemoveFrame.grid_rowconfigure(4, weight=1)


        #----------------------- MODIFY PRODUCT -----------------------
        # labels
        self.productNameLabel = CTkLabel(self.modifyItemModifyFrame, text="Product Name:") 
        self.categoryLabel = CTkLabel(self.modifyItemModifyFrame, text="Category:") 
        self.inStockLabel = CTkLabel(self.modifyItemModifyFrame, text="Current Stock:") 
        self.buyingPriceLabel = CTkLabel(self.modifyItemModifyFrame, text="Buying Price:") 
        self.sellingPriceLabel = CTkLabel(self.modifyItemModifyFrame, text="Selling Price:") 

        # modify frame label grids
        self.productNameLabel.grid(row=1, column=1, sticky="w")
        self.categoryLabel.grid(row=2, column=1, sticky="w")
        self.inStockLabel.grid(row=3, column=1, sticky="w")
        self.buyingPriceLabel.grid(row=4, column=1, sticky="w")
        self.sellingPriceLabel.grid(row=5, column=1, sticky="w")

        # entry widgets
        self.productNameEntry = CTkEntry(self.modifyItemModifyFrame, placeholder_text="Enter text")
        self.categoryModifyOptionMenu = CTkOptionMenu(self.modifyItemModifyFrame, values=self.get_category_list())
        self.inStockEntry = CTkEntry(self.modifyItemModifyFrame, placeholder_text="Enter integer")
        self.buyingPriceEntry = CTkEntry(self.modifyItemModifyFrame, placeholder_text="Enter integer")
        self.sellingPriceEntry = CTkEntry(self.modifyItemModifyFrame, placeholder_text="Enter integer")

        # modify tab entry widgets grids
        self.productNameEntry.grid(row=1, column=3, sticky="ew")
        self.categoryModifyOptionMenu.grid(row=2, column=3, sticky="ew")
        self.inStockEntry.grid(row=3, column=3, sticky="ew")
        self.buyingPriceEntry.grid(row=4, column=3, sticky="ew")
        self.sellingPriceEntry.grid(row=5, column=3, sticky="ew")

        # modify tab discard button
        self.discardButton = CTkButton(self.modifyItemModifyFrame, text="Discard", fg_color="#FF0F2F", hover_color="#AF0F2F", command=lambda: self.modify_item_discard())
        self.discardButton.grid(row=6, column=3, sticky="ew")

        # modify tab save button
        self.saveButton = CTkButton(self.modifyItemModifyFrame, text="Save", command=lambda: self.modify_item_save())
        self.saveButton.grid(row=6, column=1, sticky="ew")


        #------------------------- CATEGORY ADD -----------------------
        self.addCategoryLabel = CTkLabel(self.modifyItemCategoryFrame, text="Add Category:")
        self.addCategoryReplyLabel = CTkLabel(self.modifyItemCategoryFrame, text="")
        self.addCategoryEntry = CTkEntry(self.modifyItemCategoryFrame, placeholder_text="Enter category")
        self.addCategoryButton = CTkButton(self.modifyItemCategoryFrame, text="Add Category", command=lambda: self.add_category())

        self.addCategoryLabel.grid(row=1, column=1, pady=(5, 5), sticky="ew")
        self.addCategoryReplyLabel.grid(row=1, column=3, sticky="ew")
        self.addCategoryEntry.grid(row=2, column=1, columnspan=2, padx=(0, 5), pady=(5, 5), sticky="ew")
        self.addCategoryButton.grid(row=2, column=3, padx=(5, 0), pady=(5, 5), sticky="ew")

        self.removeCategoryLabel = CTkLabel(self.modifyItemCategoryFrame, text="Remove Category:")
        self.removeCategoryReplyLabel = CTkLabel(self.modifyItemCategoryFrame, text="")
        self.removeCategoryOptionMenu = CTkOptionMenu(self.modifyItemCategoryFrame, values=self.get_category_list())
        self.removeCategoryButton = CTkButton(self.modifyItemCategoryFrame, fg_color="#FF0F2F", hover_color="#AF0F2F", text="Remove Category", command=lambda: self.remove_category())

        self.removeCategoryLabel.grid(row=4, column=1, sticky="ew")
        self.removeCategoryReplyLabel.grid(row=4, column=3, sticky="ew")
        self.removeCategoryOptionMenu.grid(row=5, column=1, columnspan=2, padx=(0, 5), pady=(5, 5), sticky="ew")
        self.removeCategoryButton.grid(row=5, column=3, padx=(5, 0), pady=(5, 5), sticky="ew")
        

        #------------------------- PRODUCT ADD -----------------------
        # labels
        self.productAddNameLabel = CTkLabel(self.modifyItemAddFrame, text="Product Name:") 
        self.categoryAddLabel = CTkLabel(self.modifyItemAddFrame, text="Category:") 
        self.inStockAddLabel = CTkLabel(self.modifyItemAddFrame, text="Current Stock:") 
        self.buyingAddPriceLabel = CTkLabel(self.modifyItemAddFrame, text="Buying Price:") 
        self.sellingAddPriceLabel = CTkLabel(self.modifyItemAddFrame, text="Selling Price:") 

        # add product label grids
        self.productAddNameLabel.grid(row=1, column=1, sticky="w")
        self.categoryAddLabel.grid(row=2, column=1, sticky="w")
        self.inStockAddLabel.grid(row=3, column=1, sticky="w")
        self.buyingAddPriceLabel.grid(row=4, column=1, sticky="w")
        self.sellingAddPriceLabel.grid(row=5, column=1, sticky="w")

        # entry widgets
        self.productAddNameEntry = CTkEntry(self.modifyItemAddFrame, placeholder_text="Enter product name")
        self.categoryAddOptionMenu = CTkOptionMenu(self.modifyItemAddFrame, values=self.get_category_list())
        self.inStockAddEntry = CTkEntry(self.modifyItemAddFrame, placeholder_text="Enter current stock")
        self.buyingAddPriceEntry = CTkEntry(self.modifyItemAddFrame, placeholder_text="Enter buying price")
        self.sellingAddPriceEntry = CTkEntry(self.modifyItemAddFrame, placeholder_text="Enter selling price")

        # add product entry widgets grids
        self.productAddNameEntry.grid(row=1, column=3, sticky="ew")
        self.categoryAddOptionMenu.grid(row=2, column=3, sticky="ew")
        self.inStockAddEntry.grid(row=3, column=3, sticky="ew")
        self.buyingAddPriceEntry.grid(row=4, column=3, sticky="ew")
        self.sellingAddPriceEntry.grid(row=5, column=3, sticky="ew")

        # add product discard button
        self.discardProductAddButton = CTkButton(self.modifyItemAddFrame, text="Discard", fg_color="#FF0F2F", hover_color="#AF0F2F", command=lambda: self.modify_item_discard())
        self.discardProductAddButton.grid(row=6, column=3, sticky="ew")

        # add product save button
        self.saveProductAddButton = CTkButton(self.modifyItemAddFrame, text="Save", command=lambda: self.verify_product_add())
        self.saveProductAddButton.grid(row=6, column=1, sticky="ew")


        #------------------------- DELETE PRODUCT -------------------------
        self.deleteStatusLabel = CTkLabel(self.modifyItemRemoveFrame, text="")
        self.deleteButton = CTkButton(self.modifyItemRemoveFrame, text="Remove Product", fg_color="#FF0F2F", hover_color="#AF0F2F")
        self.deleteAllLabel = CTkLabel(self.modifyItemRemoveFrame, text="REQUIRES ADMIN ACCOUNT", font=("Arial", 13, "bold"))
        self.deleteAllButton = CTkButton(self.modifyItemRemoveFrame, text="Reset Inventory", fg_color="#FF0F2F", hover_color="#AF0F2F")

        self.deleteStatusLabel.grid(row=0, column=1, sticky="ew")
        self.deleteButton.grid(row=1, column=1)
        self.deleteAllLabel.grid(row=2, column=1)
        self.deleteAllButton.grid(row=3, column=1)

    def sort_by_column(self, column):
        self.treeView.delete(*self.treeView.get_children())
        for table in itemdata.sort_table(column, self.ascending):
            self.treeView.insert("", "end", values=table)
        self.ascending = not self.ascending

    def search(self):
        if self.searchItemEntry.get() == "":
            self.get_all_inventory()
            self.focus_set()
            return
        if not itemdata.search_product(self.searchItemEntry.get()):
            self.treeView.delete(*self.treeView.get_children())
            self.focus_set()
            return
        else:
            self.treeView.delete(*self.treeView.get_children())
            for item in itemdata.search_product(self.searchItemEntry.get()):
                self.treeView.insert("", "end", values=item)
            self.focus_set()

    def get_all_inventory(self):
        self.treeView.delete(*self.treeView.get_children())
        for item in itemdata.view_inventory():
            self.treeView.insert("", "end", values=item)

    def verify_product_add(self):
        item = self.productAddNameEntry.get()
        category = self.categoryAddOptionMenu.get()
        stock = self.inStockAddEntry.get()
        buying_price = self.buyingAddPriceEntry.get()
        selling_price = self.sellingAddPriceEntry.get()
        if item == "":
            self.statusReplyLabel.configure(text="*Product name required", text_color="#FF0000")
            return
        if stock == "":
            self.statusReplyLabel.configure(text="*Current stock required", text_color="#FF0000")
            return
        if buying_price == "":
            self.statusReplyLabel.configure(text="*Enter price value", text_color="#FF0000")
            return
        if selling_price == "":
            self.statusReplyLabel.configure(text="*Enter price value", text_color="#FF0000")
            return
        self.add_product(item, category, stock, buying_price, selling_price)

    def add_product(self, item, category, stock, buying_price, selling_price):
        match itemdata.add_product(item, category, stock, buying_price, selling_price):
            case 0:
                self.get_all_inventory()
                self.statusReplyLabel.configure(text="Product added", text_color="#00FF00")
                self.add_product_labelreset()
            case 1:
                self.statusReplyLabel.configure(text="Product not added", text_color="#FF0000")
                self.add_product_labelreset()

    def add_product_labelreset(self):
        self.productAddNameEntry.delete(0, 'end')
        self.inStockAddEntry.delete(0, 'end')
        self.buyingAddPriceEntry.delete(0, 'end')
        self.sellingAddPriceEntry.delete(0, 'end')
        self.focus_set()

    def get_category_list(self):
        categories = itemdata.get_all_category()
        if categories:
            return [""] + [str(item[0]) for item in categories]
        return [""]

    def add_category(self):
        category = self.addCategoryEntry.get()
        if category == "":
            self.addCategoryReplyLabel.configure(text="*Category field required", text_color="#FF0000")
            return
        match itemdata.add_category(category):
            case 0:
                self.refresh_categories()
                self.addCategoryReplyLabel.configure(text="*Category added", text_color="#00AA00")
                self.addCategoryEntry.delete(0, 'end')
                self.focus_set()
            case 1:
                self.addCategoryReplyLabel.configure(text="*Category already exists", text_color="#FF0000")
                self.addCategoryEntry.delete(0, 'end')
                self.focus_set()
            case _:
                self.addCategoryReplyLabel.configure(text="*Unknown error", text_color="#FF0000")
                self.addCategoryEntry.delete(0, 'end')
                self.focus_set()

    def remove_category(self):
        remove_category = self.removeCategoryOptionMenu.get()
        if remove_category == "":
            self.removeCategoryReplyLabel.configure(text="*Select category", text_color="#FF0000")
            return
        itemdata.remove_category(remove_category)
        self.removeCategoryReplyLabel.configure(text="*Category removed", text_color="#00AA00")
        self.refresh_categories()

    def reload_treeview(self):
        self.table.change_theme(settings.table_theme_read())

    def refresh_categories(self):
        self.removeCategoryOptionMenu.configure(variable="", values=self.get_category_list())
        self.categoryModifyOptionMenu.configure(variable="", values=self.get_category_list())
        self.categoryAddOptionMenu.configure(variable="", values=self.get_category_list())

    def modify_item_discard(self):
        print("Discard changes")

    def modify_item_save(self):
        print("Save Item")

