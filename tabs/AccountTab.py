from customtkinter import CTkButton, CTkFrame, CTkImage, CTkLabel
from PIL import Image
from utils import accounts, randompic, Assets
from pathlib import Path
from tkinter import Canvas

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
        self.accountPicture.grid(row=0, column=0, rowspan=2, columnspan=2, padx=(10, 10), pady=(10, 10), sticky="nw")
        self.accountPicture.grid_columnconfigure(0, weight=1)
        self.accountPicture.grid_rowconfigure(0, weight=1)

        self.profilePicture = CTkImage(
                light_image=Image.open(self.get_picture()),
                dark_image=Image.open(self.get_picture()),
                size=(128, 128))
        self.profilePictureLabel = CTkLabel(self.accountPicture, image=self.profilePicture, text="")
        self.profilePictureLabel.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.accountNameLabel = CTkLabel(self.accountSettingsFrame, text=str(accounts.get_session()), font=("Roboto", 30, "bold"))
        self.accountNameLabel.grid(row=0, column=2, columnspan=3, padx=(10, 10), pady=(10, 10), sticky="nw")

        self.changeProfilePictureButton = CTkButton(self.accountSettingsFrame, text="Change Photo", command=lambda: self.change_profile_picture())
        self.changeProfilePictureButton.grid(row=2, column=0)

        self.changeLabelButton = CTkButton(self.accountSettingsFrame, text="Refresh Account", command=self.update_account_name())
        self.changeLabelButton.grid(row=3, column=0)

        # create frame for list accounts
        self.accountListFrame = CTkFrame(self)
        self.accountListFrame.grid(row=0, column=2, rowspan=4, columnspan=2, padx=(5, 10), pady=(10, 10), sticky="nsew")

    def update_account_name(self):
        self.accountNameLabel.configure(text=str(accounts.get_session()))

    def get_picture(self):
        if accounts.get_session() == None:
            return Path("assets/image/admin.png")
        return Path("assets/image") / (str(accounts.get_session()) + ".png")

    def change_profile_picture(self):
        randompic.generate_box_image(str(accounts.get_session()))
        self.profilePicture = CTkImage(
                light_image=Image.open(self.get_picture()),
                dark_image=Image.open(self.get_picture()),
                size=(128, 128))
        self.profilePictureLabel = CTkLabel(self.accountPicture, image=self.profilePicture, text="")
