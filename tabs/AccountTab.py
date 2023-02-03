from customtkinter import CTkButton, CTkFrame, CTkImage, CTkLabel
from PIL import Image
from utils import accounts, randompic
from pathlib import Path

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

        self.accountSettingsFrame.grid_columnconfigure(0, weight=0)
        self.accountSettingsFrame.grid_columnconfigure(1, weight=0)
        self.accountSettingsFrame.grid_columnconfigure(2, weight=0)
        self.accountSettingsFrame.grid_rowconfigure(0, weight=0)
        self.accountSettingsFrame.grid_rowconfigure(1, weight=0)
        self.accountSettingsFrame.grid_rowconfigure(2, weight=0)
        self.accountSettingsFrame.grid_rowconfigure(3, weight=0)
        self.accountSettingsFrame.grid_rowconfigure(4, weight=1)
        self.accountSettingsFrame.grid_rowconfigure(5, weight=1)
        self.accountSettingsFrame.grid_rowconfigure(6, weight=1)
        
        self.accountPicture = CTkFrame(self.accountSettingsFrame) 
        self.accountPicture.grid(row=0, column=0, rowspan=3, columnspan=2, padx=(10, 10), pady=(10, 10), sticky="")
        self.accountPicture.grid_columnconfigure(0, weight=1)
        self.accountPicture.grid_rowconfigure(0, weight=1)

        self.profilePicture = CTkImage(
                light_image=Image.open(self.get_picture()),
                dark_image=Image.open(self.get_picture()),
                size=(128, 128))
        self.profilePictureLabel = CTkLabel(self.accountPicture, image=self.profilePicture, text="")
        self.profilePictureLabel.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.accountNameLabel = CTkLabel(self.accountSettingsFrame, text=self.show_current_session(), font=("Arial", 30, "bold"))
        self.accountNameLabel.grid(row=0, column=2, columnspan=1, padx=(10, 10), pady=(10, 10), sticky="")

        self.permissionLevelLabel = CTkLabel(self.accountSettingsFrame, text="Permission level", font=("Arial", 14, "bold"))
        self.permissionLevelLabel.grid(row=1, column=2, columnspan=1, padx=(10, 10), pady=(10, 10), sticky="n")

        self.changeProfilePictureButton = CTkButton(self.accountSettingsFrame, text="Change Photo", command=lambda: self.change_profile_picture())
        self.changeProfilePictureButton.grid(row=3, column=0, columnspan=2, sticky="n")

        self.changeLabelButton = CTkButton(self.accountSettingsFrame, text="Refresh Account", command=lambda: self.refresh_account())
        self.changeLabelButton.grid(row=4, column=0, columnspan=2)

        # create frame for list accounts
        self.accountListFrame = CTkFrame(self)
        self.accountListFrame.grid(row=0, column=2, rowspan=4, columnspan=2, padx=(5, 10), pady=(10, 10), sticky="nsew")


    def show_current_session(self):
        return str(accounts.get_session())

    def refresh_account(self):
        self.accountNameLabel.configure(text=self.show_current_session())
        self.refresh_picture()
        self.show_permission_level()

    def get_picture(self):
        if accounts.get_session() == None:
            return Path("assets/image/admin.png")
        return Path("assets/image") / (self.show_current_session() + ".png")

    def change_profile_picture(self):
        randompic.generate_box_image(self.show_current_session())
        self.refresh_picture()

    def refresh_picture(self):
        self.profilePicture.configure(
                light_image=Image.open(self.get_picture()),
                dark_image=Image.open(self.get_picture()),
                size=(128, 128))
        self.profilePictureLabel.configure(image=self.profilePicture, text="")

    def show_permission_level(self):
        if accounts.get_permission_level(str(accounts.get_session())):
            self.permissionLevelLabel.configure(text="Administrator")
        else:
            self.permissionLevelLabel.configure(text="User")
