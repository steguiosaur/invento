from customtkinter import CTkFrame, CTkTabview, CTkLabel, CTkEntry, CTkButton, CTkOptionMenu
from customwidget import IntSpinbox, CtmTreeView
from utils import settings

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
        self.table = CtmTreeView(self, theme=settings.table_theme_read())
        self.table.grid(row=0, column=0, rowspan=3, columnspan=4, padx=(10, 10), pady=(10, 5), sticky="nsew")

        # create product table
        self.treeView = self.table.get_treeview()
        self.treeView["show"] = "headings"
        self.treeView["columns"] = (1, 2, 3, 4, 5, 6)
        
        self.treeView.column(1, width=100)
        self.treeView.column(2, width=70)
        self.treeView.column(3, width=30)
        self.treeView.column(4, width=30)
        self.treeView.column(5, width=30)
        self.treeView.column(6, width=30)

        self.treeView.heading(1, text="Product Name")
        self.treeView.heading(2, text="Category")
        self.treeView.heading(3, text="In-Stock")
        self.treeView.heading(4, text="Buying Price")
        self.treeView.heading(5, text="Selling Price")
        self.treeView.heading(6, text="Date Modified")

        # create frame for search items
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
        self.searchItemEntry = CTkEntry(self.searchItemFrame)
        self.searchItemEntry.grid(row=0, column=0, columnspan=4, padx=(10, 5), pady=(10, 5), sticky="ew")

        self.searchItemButton = CTkButton(self.searchItemFrame, text="Search", command=lambda: print("search"))
        self.searchItemButton.grid(row=0, column=4, padx=(5, 10), pady=(10, 5), sticky="ew")

        # status frame
        self.statusLabel = CTkLabel(self.searchItemFrame, text="")
        self.statusLabel.grid(row=1, column=0, columnspan=5)

        # frame for sales
        self.salesFrame = CTkFrame(self.searchItemFrame)
        self.salesFrame.grid(row=2, column=0, columnspan=5, rowspan=3, padx=(10, 10), pady=(5, 10), sticky="nsew")

        self.salesFrame.grid_columnconfigure(0, weight=1)
        self.salesFrame.grid_columnconfigure(1, weight=1)
        self.salesFrame.grid_columnconfigure(2, weight=1)
        self.salesFrame.grid_columnconfigure(3, weight=1)
        self.salesFrame.grid_columnconfigure(4, weight=1)
        self.salesFrame.grid_rowconfigure(0, weight=1)
        self.salesFrame.grid_rowconfigure(1, weight=1)
        self.salesFrame.grid_rowconfigure(2, weight=1)
        self.salesFrame.grid_rowconfigure(3, weight=1)
        self.salesFrame.grid_rowconfigure(4, weight=1)

        self.salesLabel = CTkLabel(self.salesFrame, text="Add Sales")
        self.salesLabel.grid(row=0, column=1)

        self.salesSpinBox = IntSpinbox(self.salesFrame, min_value=0, max_value=100, step_size=1)
        self.salesSpinBox.grid(row=1, column=1, sticky="ew")

        self.salesButton = CTkButton(self.salesFrame, text="Add", command=lambda: print("save sales"))
        self.salesButton.grid(row=2, column=1, sticky="ew")

        self.removeSalesLabel = CTkLabel(self.salesFrame, text="Remove Sales")
        self.removeSalesLabel.grid(row=0, column=3)

        self.removeSalesSpinBox = IntSpinbox(self.salesFrame, min_value=0, step_size=1)
        self.removeSalesSpinBox.grid(row=1, column=3, sticky="ew")

        self.removeSalesButton = CTkButton(self.salesFrame, text="Remove", fg_color="#FF0F2F", hover_color="#AF0F2F", command=lambda: print("remove sales"))
        self.removeSalesButton.grid(row=2, column=3, sticky="ew")

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
        self.modifyItemModifyFrame.rowconfigure(6, weight=1)
        self.modifyItemModifyFrame.rowconfigure(7, weight=1)
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
        self.productNameLabel.grid(row=1, column=1, sticky="w")
        self.categoryLabel.grid(row=2, column=1, sticky="w")
        self.inStockLabel.grid(row=3, column=1, sticky="w")
        self.buyingPriceLabel.grid(row=4, column=1, sticky="w")
        self.sellingPriceLabel.grid(row=5, column=1, sticky="w")

        # entry widgets
        self.productNameEntry = CTkEntry(self.modifyItemModifyFrame)
        self.categoryEntry = CTkOptionMenu(self.modifyItemModifyFrame)
        self.inStockEntry = CTkEntry(self.modifyItemModifyFrame)
        self.buyingPriceEntry = CTkEntry(self.modifyItemModifyFrame)
        self.sellingPriceEntry = CTkEntry(self.modifyItemModifyFrame)

        # modify tab entry widgets grids
        self.productNameEntry.grid(row=1, column=3, sticky="ew")
        self.categoryEntry.grid(row=2, column=3, sticky="ew")
        self.inStockEntry.grid(row=3, column=3, sticky="ew")
        self.buyingPriceEntry.grid(row=4, column=3, sticky="ew")
        self.sellingPriceEntry.grid(row=5, column=3, sticky="ew")

        # modify tab discard button
        self.discardButton = CTkButton(self.modifyItemModifyFrame, text="Discard", fg_color="#FF0F2F", hover_color="#AF0F2F", command=lambda: self.modify_item_discard())
        self.discardButton.grid(row=6, column=3, sticky="ew")

        # modify tab save button
        self.saveButton = CTkButton(self.modifyItemModifyFrame, text="Save", command=lambda: self.modify_item_save())
        self.saveButton.grid(row=6, column=1, sticky="ew")


        # category tab grid
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

        self.addCategoryLabel = CTkLabel(self.modifyItemCategoryFrame, text="Add Category:")
        self.addCategoryReplyLabel = CTkLabel(self.modifyItemCategoryFrame, text="")
        self.addCategoryEntry = CTkEntry(self.modifyItemCategoryFrame)
        self.addCategoryButton = CTkButton(self.modifyItemCategoryFrame, text="Add Category", command=lambda: print("added category"))

        self.addCategoryLabel.grid(row=1, column=1, pady=(5, 5), sticky="ew")
        self.addCategoryReplyLabel.grid(row=1, column=2, columnspan=2, pady=(5, 5), sticky="ew")
        self.addCategoryEntry.grid(row=2, column=1, columnspan=2, padx=(0, 5), pady=(5, 5), sticky="ew")
        self.addCategoryButton.grid(row=2, column=3, padx=(5, 0), pady=(5, 5), sticky="ew")

        self.removeCategoryLabel = CTkLabel(self.modifyItemCategoryFrame, text="Remove Category:")
        self.removeCategoryReplyLabel = CTkLabel(self.modifyItemCategoryFrame, text="")
        self.removeCategoryOptionMenu = CTkOptionMenu(self.modifyItemCategoryFrame)
        self.removeCategoryButton = CTkButton(self.modifyItemCategoryFrame, text="Remove Category", command=lambda: print("removed category"))

        self.removeCategoryLabel.grid(row=4, column=1, pady=(5, 5), sticky="ew")
        self.removeCategoryReplyLabel.grid(row=4, column=2, columnspan=2, pady=(5, 5), sticky="ew")
        self.removeCategoryOptionMenu.grid(row=5, column=1, columnspan=2, padx=(0, 5), pady=(5, 5), sticky="ew")
        self.removeCategoryButton.grid(row=5, column=3, padx=(5, 0), pady=(5, 5), sticky="ew")
        

        # add product tab grids
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
        
        # labels
        self.productNameLabel = CTkLabel(self.modifyItemAddFrame, text="Product Name:") 
        self.categoryLabel = CTkLabel(self.modifyItemAddFrame, text="Category:") 
        self.inStockLabel = CTkLabel(self.modifyItemAddFrame, text="Current Stock:") 
        self.buyingPriceLabel = CTkLabel(self.modifyItemAddFrame, text="Buying Price:") 
        self.sellingPriceLabel = CTkLabel(self.modifyItemAddFrame, text="Selling Price:") 

        # add product label grids
        self.productNameLabel.grid(row=1, column=1, sticky="w")
        self.categoryLabel.grid(row=2, column=1, sticky="w")
        self.inStockLabel.grid(row=3, column=1, sticky="w")
        self.buyingPriceLabel.grid(row=4, column=1, sticky="w")
        self.sellingPriceLabel.grid(row=5, column=1, sticky="w")

        # entry widgets
        self.productNameEntry = CTkEntry(self.modifyItemAddFrame)
        self.categoryEntry = CTkOptionMenu(self.modifyItemAddFrame)
        self.inStockEntry = CTkEntry(self.modifyItemAddFrame)
        self.buyingPriceEntry = CTkEntry(self.modifyItemAddFrame)
        self.sellingPriceEntry = CTkEntry(self.modifyItemAddFrame)

        # add product entry widgets grids
        self.productNameEntry.grid(row=1, column=3, sticky="ew")
        self.categoryEntry.grid(row=2, column=3, sticky="ew")
        self.inStockEntry.grid(row=3, column=3, sticky="ew")
        self.buyingPriceEntry.grid(row=4, column=3, sticky="ew")
        self.sellingPriceEntry.grid(row=5, column=3, sticky="ew")

        # add product discard button
        self.discardButton = CTkButton(self.modifyItemAddFrame, text="Discard", fg_color="#FF0F2F", hover_color="#AF0F2F", command=lambda: self.modify_item_discard())
        self.discardButton.grid(row=6, column=3, sticky="ew")

        # add product save button
        self.saveButton = CTkButton(self.modifyItemAddFrame, text="Save", command=self.modify_item_save)
        self.saveButton.grid(row=6, column=1, sticky="ew")


        # delete product tab
        self.modifyItemRemoveFrame.grid_columnconfigure(0, weight=1)
        self.modifyItemRemoveFrame.grid_columnconfigure(1, weight=1)
        self.modifyItemRemoveFrame.grid_columnconfigure(2, weight=1)
        self.modifyItemRemoveFrame.grid_rowconfigure(0, weight=1)
        self.modifyItemRemoveFrame.grid_rowconfigure(1, weight=1)
        self.modifyItemRemoveFrame.grid_rowconfigure(2, weight=1)
        self.modifyItemRemoveFrame.grid_rowconfigure(3, weight=1)
        self.modifyItemRemoveFrame.grid_rowconfigure(4, weight=1)

        self.deleteButton = CTkButton(self.modifyItemRemoveFrame, text="Remove Product")
        self.deleteAllLabel = CTkLabel(self.modifyItemRemoveFrame, text="requires admin privileges")
        self.deleteAllButton = CTkButton(self.modifyItemRemoveFrame, text="Reset Inventory")

        self.deleteButton.grid(row=1, column=1)
        self.deleteAllLabel.grid(row=2, column=1)
        self.deleteAllButton.grid(row=3, column=1)

    def modify_item_discard(self):
        print("Discard changes")

    def modify_item_save(self):
        print("Save Item")

