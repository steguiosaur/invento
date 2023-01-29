from customtkinter import CTkFrame

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
        self.displayAddedProductFrame = CTkFrame(self)
        self.displayAddedProductFrame.grid(row=2, column=1, rowspan=2, columnspan=3, padx=(5, 10), pady=(5, 10), sticky="nsew")
