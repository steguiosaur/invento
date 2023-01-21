from customtkinter import CTkFrame

class DashboardTab(CTkFrame):
    def __init__(self, parent):
        CTkFrame.__init__(self, parent)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(11, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(3, weight=1)

        # create frame for 

        # create frame for account settings
        self.displayUserFrame = CTkFrame(self)
        self.displayUserFrame.grid(row=0, column=0, rowspan=4, columnspan=2, padx=(10, 10), pady=(10, 10), sticky="nsew")

        # create frame for list accounts
        self.displayNumcCategoryFrame = CTkFrame(self)
        self.displayNumcCategoryFrame.grid(row=0, column=2, rowspan=4, columnspan=2, padx=(10, 10), pady=(10, 10), sticky="nsew")

        # create frame for list accounts
        self.displayNumProductsFrame = CTkFrame(self)
        self.displayNumProductsFrame.grid(row=0, column=2, rowspan=4, columnspan=2, padx=(10, 10), pady=(10, 10), sticky="nsew")

        # create frame for list accounts
        self.displayNumSalesFrame = CTkFrame(self)
        self.displayNumSalesFrame.grid(row=0, column=2, rowspan=4, columnspan=2, padx=(10, 10), pady=(10, 10), sticky="nsew")

        # create frame for list accounts
        self.displaySalesGraphFrame = CTkFrame(self)
        self.displaySalesGraphFrame.grid(row=0, column=2, rowspan=4, columnspan=2, padx=(10, 10), pady=(10, 10), sticky="nsew")

        # create frame for list accounts
        self.displayAddedProductFrame = CTkFrame(self)
        self.displayAddedProductFrame.grid(row=0, column=2, rowspan=4, columnspan=2, padx=(10, 10), pady=(10, 10), sticky="nsew")
