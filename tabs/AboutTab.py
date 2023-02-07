from customtkinter import CTkFrame, CTkImage, CTkLabel, CTkScrollableFrame
from utils import Assets
from PIL import Image

class AboutTab(CTkFrame):
    def __init__(self, parent):
        CTkFrame.__init__(self, parent)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # create frame for about section
        self.aboutPageFrame = CTkScrollableFrame(self)
        self.aboutPageFrame.grid(row=0, column=0, rowspan=4, columnspan=4, padx=(10, 10), pady=(10, 10), sticky="nsew")
        self.aboutPageFrame.grid_columnconfigure(0, weight=1)
        self.aboutPageFrame.grid_columnconfigure(1, weight=1)
        self.aboutPageFrame.grid_columnconfigure(2, weight=1)
        self.aboutPageFrame.grid_rowconfigure(0, weight=1)
        self.aboutPageFrame.grid_rowconfigure(1, weight=1)
        self.aboutPageFrame.grid_rowconfigure(2, weight=1)
        self.aboutPageFrame.grid_rowconfigure(3, weight=1)
        self.aboutPageFrame.grid_rowconfigure(4, weight=1)
        self.aboutPageFrame.grid_rowconfigure(5, weight=1)

        # application logo
        self.logoImg = CTkImage(
            light_image=Image.open(Assets.asset_path("./light_bg_logo.png")),
            dark_image=Image.open(Assets.asset_path("./dark_bg_logo.png")),
            size=(268, 75))
        self.logoImgLabel=CTkLabel(self.aboutPageFrame, image=self.logoImg, text="")
        self.logoImgLabel.grid(row=0, column=1)
