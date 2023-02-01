from customtkinter import CTkFrame, CTkLabel

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
        self.accountSettingsFrame.grid(row=0, column=0, rowspan=4, columnspan=2, padx=(10, 5), pady=(10, 10), sticky="nsew")

        self.accountSettingsFrame.grid_columnconfigure(0, weight=1)
        self.accountSettingsFrame.grid_columnconfigure(1, weight=1)
        self.accountSettingsFrame.grid_columnconfigure(2, weight=1)
        self.accountSettingsFrame.grid_columnconfigure(3, weight=1)
        self.accountSettingsFrame.grid_columnconfigure(4, weight=1)
        self.accountSettingsFrame.grid_rowconfigure(0, weight=1)
        self.accountSettingsFrame.grid_rowconfigure(1, weight=1)
        self.accountSettingsFrame.grid_rowconfigure(2, weight=1)
        self.accountSettingsFrame.grid_rowconfigure(3, weight=1)
        self.accountSettingsFrame.grid_rowconfigure(4, weight=1)
        self.accountSettingsFrame.grid_rowconfigure(5, weight=1)
        self.accountSettingsFrame.grid_rowconfigure(6, weight=1)
        
        self.accountPicture = CTkFrame(self.accountSettingsFrame) 
        self.accountPicture.grid(row=0, column=0, rowspan=2, columnspan=2, padx=(10, 10), pady=(10, 10), sticky="nsew")

        self.accountNameLabel = CTkLabel(self.accountSettingsFrame, text="", font=("Roboto", 30, "bold"))
        self.accountNameLabel.grid(row=0, column=2, columnspan=3, padx=(10, 10), pady=(10, 10), sticky="nw")

        # create frame for list accounts
        self.accountListFrame = CTkFrame(self)
        self.accountListFrame.grid(row=0, column=2, rowspan=4, columnspan=2, padx=(5, 10), pady=(10, 10), sticky="nsew")
