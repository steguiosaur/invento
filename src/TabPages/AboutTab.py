from customtkinter import CTkFrame

class AboutTab(CTkFrame):
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

        # create frame for about section
        self.aboutPageFrame = CTkFrame(self)
        self.aboutPageFrame.grid(row=0, column=0, rowspan=4, columnspan=4, padx=(10, 10), pady=(10, 10), sticky="nsew")

