from customtkinter import CTkFrame, CTkImage, CTkLabel, CENTER
from PIL import Image
from utils import Assets

class LoginBg(CTkFrame):
    def __init__(self, parent):
        CTkFrame.__init__(self, parent)

        # background image for login
        self.bgImg = CTkImage(
            light_image=Image.open(Assets.asset_path("./light_bg.jpg")),
            dark_image=Image.open(Assets.asset_path("./dark_bg.jpg")),
            size=(1920, 1080))
        self.bgImgLabel=CTkLabel(self, image=self.bgImg, text="")
        self.bgImgLabel.pack(anchor="ne")

        # login entry frame
        self.loginFrame = CTkFrame(self, width=640, height=360, corner_radius=0)
        self.loginFrame.place(relx=0.5, rely=0.5, anchor=CENTER)

        # application logo
        self.logoImg = CTkImage(
            light_image=Image.open(Assets.asset_path("./light_bg_logo.png")),
            dark_image=Image.open(Assets.asset_path("./dark_bg_logo.png")),
            size=(264, 75))
        self.logoImgLabel=CTkLabel(self.loginFrame, image=self.logoImg, text="")
        self.logoImgLabel.place(relx=0.28, rely=0.5, anchor=CENTER)
