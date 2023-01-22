from customtkinter import CTkFrame

class AccountTab(CTkFrame):
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
        self.accountSettingsFrame = CTkFrame(self)
        self.accountSettingsFrame.grid(row=0, column=0, rowspan=4, columnspan=2, padx=(10, 10), pady=(10, 10), sticky="nsew")

        # create frame for list accounts
        self.accountListFrame = CTkFrame(self)
        self.accountListFrame.grid(row=0, column=2, rowspan=4, columnspan=2, padx=(10, 10), pady=(10, 10), sticky="nsew")
