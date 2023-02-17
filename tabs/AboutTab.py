from customtkinter import CTkFrame, CTkImage, CTkLabel
from utils import Assets
from PIL import Image

class AboutTab(CTkFrame):
    def __init__(self, parent):
        CTkFrame.__init__(self, parent)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # create frame for about section
        self.aboutPageFrame = CTkFrame(self)
        self.aboutPageFrame.grid(row=0, column=0, rowspan=4, columnspan=4, padx=(10, 10), pady=(10, 10), sticky="nsew")
        self.aboutPageFrame.grid_columnconfigure(0, weight=1)
        self.aboutPageFrame.grid_columnconfigure(1, weight=1)
        self.aboutPageFrame.grid_columnconfigure(2, weight=1)
        self.aboutPageFrame.grid_columnconfigure(3, weight=1)
        self.aboutPageFrame.grid_rowconfigure(0, weight=0)
        self.aboutPageFrame.grid_rowconfigure(1, weight=1)
        self.aboutPageFrame.grid_rowconfigure(2, weight=0)
        self.aboutPageFrame.grid_rowconfigure(3, weight=0)
        self.aboutPageFrame.grid_rowconfigure(4, weight=0)
        self.aboutPageFrame.grid_rowconfigure(5, weight=1)
        self.aboutPageFrame.grid_rowconfigure(6, weight=1)
        self.aboutPageFrame.grid_rowconfigure(7, weight=1)

        # application logo
        self.logoImg = CTkImage(
            light_image=Image.open(Assets.asset_path("./light_bg_logo.png")),
            dark_image=Image.open(Assets.asset_path("./dark_bg_logo.png")),
            size=(268, 75))
        self.logoImgLabel=CTkLabel(self.aboutPageFrame, image=self.logoImg, text="")
        self.logoImgLabel.grid(row=1, column=1, columnspan=2)

        self.aboutText1 = CTkLabel(self.aboutPageFrame, text="Invento is an inventory management system that helps")
        self.aboutText2 = CTkLabel(self.aboutPageFrame, text="small business owners manage their inventories and sales per day.")
        self.aboutText3 = CTkLabel(self.aboutPageFrame, text="This project is made using Python.")
        self.aboutText1.grid(row=2, column=1, columnspan=2)
        self.aboutText2.grid(row=3, column=1, columnspan=2)
        self.aboutText3.grid(row=4, column=1, columnspan=2)

        self.featuresFrame = CTkFrame(self.aboutPageFrame)
        self.featuresFrame.grid(row=6, column=2, columnspan=2, rowspan=2, padx=(5, 10), pady=(5, 10), sticky="nsew")
        self.featuresFrame.grid_columnconfigure(0, weight=1)
        self.featuresFrame.grid_columnconfigure(1, weight=1)
        self.featuresFrame.grid_columnconfigure(2, weight=1)
        self.featuresFrame.grid_rowconfigure(0, weight=1)
        self.featuresFrame.grid_rowconfigure(2, weight=1)
        self.featuresFrame.grid_rowconfigure(7, weight=1)
        self.featuresFrame.grid_rowconfigure(10, weight=1)

        self.aboutText4 = CTkLabel(self.featuresFrame, text="CORE FEATURES", font=("Helvetica", 14, "bold"))
        self.aboutText5 = CTkLabel(self.featuresFrame, text="- Inventory Management")
        self.aboutText6 = CTkLabel(self.featuresFrame, text="- Sales Management")
        self.aboutText7 = CTkLabel(self.featuresFrame, text="- Graph Sales")
        self.aboutText8 = CTkLabel(self.featuresFrame, text="- Account Management")
        self.aboutText16 = CTkLabel(self.featuresFrame, text="EXTRAS", font=("Helvetica", 14, "bold"))
        self.aboutText17 = CTkLabel(self.featuresFrame, text="- Change Theme and Scaling")

        self.aboutText4.grid(row=1, column=1)
        self.aboutText5.grid(row=3, column=1, sticky="w")
        self.aboutText6.grid(row=4, column=1, sticky="w")
        self.aboutText7.grid(row=5, column=1, sticky="w")
        self.aboutText8.grid(row=6, column=1, sticky="w")
        self.aboutText16.grid(row=8, column=1)
        self.aboutText17.grid(row=9, column=1, sticky="w")

        self.teamFrame = CTkFrame(self.aboutPageFrame)
        self.teamFrame.grid(row=6, column=0, columnspan=2, rowspan=2, padx=(10, 5), pady=(5, 10), sticky="nsew")
        self.teamFrame.grid_columnconfigure(0, weight=1)
        self.teamFrame.grid_columnconfigure(1, weight=1)
        self.teamFrame.grid_columnconfigure(2, weight=1)
        self.teamFrame.grid_rowconfigure(0, weight=1)
        self.teamFrame.grid_rowconfigure(2, weight=1)
        self.teamFrame.grid_rowconfigure(9, weight=1)

        self.aboutText9 = CTkLabel(self.teamFrame, text="PROJECT TEAM ROLES", font=("Helvetica", 14, "bold"))
        self.aboutText10 = CTkLabel(self.teamFrame, text="Project Manager - Annalyn Belen")
        self.aboutText11 = CTkLabel(self.teamFrame, text="Designer - Monika Jea Ng")
        self.aboutText12 = CTkLabel(self.teamFrame, text="Software Developer - Steve Pabular")
        self.aboutText13 = CTkLabel(self.teamFrame, text="Systems Analyst - John Nicolas Oandasan")
        self.aboutText14 = CTkLabel(self.teamFrame, text="Business Analyst - Hazel Concepcion")
        self.aboutText15 = CTkLabel(self.teamFrame, text="Technical Writer - Percian Cayaban")

        self.aboutText9.grid(row=1, column=1)
        self.aboutText10.grid(row=3, column=1, sticky="w")
        self.aboutText11.grid(row=4, column=1, sticky="w")
        self.aboutText12.grid(row=5, column=1, sticky="w")
        self.aboutText13.grid(row=6, column=1, sticky="w")
        self.aboutText14.grid(row=7, column=1, sticky="w")
        self.aboutText15.grid(row=8, column=1, sticky="w")

