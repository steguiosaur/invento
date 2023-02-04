from customtkinter import CTkButton, CTkFrame, CTkImage, CTkLabel, CTkEntry
from customwidget import CtmTreeView
from PIL import Image
from utils import accounts, randompic, settings
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
        self.accountSettingsFrame.grid_columnconfigure(2, weight=1)
        self.accountSettingsFrame.grid_rowconfigure(0, weight=0)
        self.accountSettingsFrame.grid_rowconfigure(1, weight=0)
        self.accountSettingsFrame.grid_rowconfigure(2, weight=0)
        self.accountSettingsFrame.grid_rowconfigure(3, weight=0)
        self.accountSettingsFrame.grid_rowconfigure(4, weight=0)
        self.accountSettingsFrame.grid_rowconfigure(5, weight=1)
        self.accountSettingsFrame.grid_rowconfigure(6, weight=1)
        
        self.accountPicture = CTkFrame(self.accountSettingsFrame) 
        self.accountPicture.grid(row=0, column=0, rowspan=4, columnspan=2, padx=(10, 10), pady=(10, 10), sticky="")
        self.accountPicture.grid_columnconfigure(0, weight=1)
        self.accountPicture.grid_rowconfigure(0, weight=1)

        self.profilePicture = CTkImage(
                light_image=Image.open(self.get_picture()),
                dark_image=Image.open(self.get_picture()),
                size=(128, 128))
        self.profilePictureLabel = CTkLabel(self.accountPicture, image=self.profilePicture, text="")
        self.profilePictureLabel.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.accountNameLabel = CTkLabel(self.accountSettingsFrame, text=self.show_current_session(), font=("Arial", 30, "bold"))
        self.accountNameLabel.grid(row=0, column=2, columnspan=1, padx=(5, 5), sticky="sw")

        self.permissionLevelLabel = CTkLabel(self.accountSettingsFrame, text="Permission level", font=("Arial", 14, "bold"))
        self.show_permission_level()
        self.permissionLevelLabel.grid(row=1, column=2, padx=(5, 5), sticky="nw")

        self.changeProfilePictureButton = CTkButton(self.accountSettingsFrame, text="Change Photo", command=lambda: self.change_profile_picture())
        self.changeProfilePictureButton.grid(row=4, column=0, columnspan=2, sticky="n")

        self.accountConfigFrame = CTkFrame(self.accountSettingsFrame)
        self.accountConfigFrame.grid(row=5, column=0, rowspan=2, columnspan=3, padx=10, pady=10, sticky="nsew")
        self.accountConfigFrame.grid_columnconfigure(0, weight=1)
        self.accountConfigFrame.grid_columnconfigure(1, weight=1)
        self.accountConfigFrame.grid_columnconfigure(2, weight=1)
        self.accountConfigFrame.grid_columnconfigure(3, weight=1)
        self.accountConfigFrame.grid_rowconfigure(0, weight=0)
        self.accountConfigFrame.grid_rowconfigure(1, weight=1)
        self.accountConfigFrame.grid_rowconfigure(2, weight=1)
        self.accountConfigFrame.grid_rowconfigure(3, weight=1)

        self.accountSettingsLabel = CTkLabel(self.accountConfigFrame, text="Account Settings", font=("Arial", 13, "bold"))
        self.accountSettingsLabel.grid(row=0, column=0, columnspan=4, padx=(5, 5), sticky="")

        self.changePasswordLabel = CTkLabel(self.accountConfigFrame, text="Change Password:")
        self.changePasswordLabel.grid(row=1, column=0, padx=(5, 5), sticky="ew")

        self.currentPasswordEntry = CTkEntry(self.accountConfigFrame)
        self.currentPasswordEntry.grid(row=1, column=1, sticky="ew")

        self.newPasswordEntry = CTkEntry(self.accountConfigFrame)
        self.newPasswordEntry.grid(row=2, column=1, sticky="ew")

        self.savePasswordEntry = CTkButton(self.accountConfigFrame)
        self.savePasswordEntry.grid(row=3, column=1, sticky="ew")

        # create frame for list accounts
        self.accountListFrame = CTkFrame(self)
        self.accountListFrame.grid(row=0, column=2, rowspan=2, columnspan=2, padx=(5, 10), pady=(10, 5), sticky="nsew")
        self.accountListFrame.grid_columnconfigure(0, weight=1)
        self.accountListFrame.grid_rowconfigure(0, weight=0)
        self.accountListFrame.grid_rowconfigure(1, weight=0)
        self.accountListFrame.grid_rowconfigure(2, weight=0)
        self.accountListFrame.grid_rowconfigure(3, weight=1)

        self.accountList = CTkLabel(self.accountListFrame, text="Account List", font=("Arial", 13, "bold"))
        self.accountList.grid(row=0, column=0)

        self.accountTable = CtmTreeView(self.accountListFrame, theme=settings.table_theme_read())
        self.accountTable.grid(row=1, column=0, rowspan=4, sticky="nsew")
        self.accountTreeview = self.accountTable.get_treeview()
        self.accountTreeview["show"] = "headings"
        self.accountTreeview["columns"] = ("1", "2")
        self.accountTreeview.column("1", width=100, anchor="center")
        self.accountTreeview.column("2", width=100, anchor="center")
        self.accountTreeview.heading("1", text="Account Name")
        self.accountTreeview.heading("2", text="Administrator")
        self.get_all_accounts()
        self.accountTreeview.bind("<<TreeviewSelect>>", self.on_select())


        self.adminSettingsFrame = CTkFrame(self)
        self.adminSettingsFrame.grid(row=2, column=2, rowspan=2, columnspan=2, padx=(5, 10), pady=(5, 10), sticky="nsew")
        self.adminSettingsFrame.grid_columnconfigure(0, weight=1)
        self.adminSettingsFrame.grid_columnconfigure(1, weight=1)
        self.adminSettingsFrame.grid_columnconfigure(2, weight=1)
        self.adminSettingsFrame.grid_rowconfigure(0, weight=1)
        self.adminSettingsFrame.grid_rowconfigure(1, weight=1)
        self.adminSettingsFrame.grid_rowconfigure(2, weight=1)
        self.adminSettingsFrame.grid_rowconfigure(3, weight=1)

        self.adminSettingsLabel = CTkLabel(self.adminSettingsFrame, text="Administrator Settings", font=("Arial", 13, "bold"))
        self.adminSettingsLabel.grid(row=0, column=0, columnspan=3, sticky="")

        self.removeUserButton = CTkButton(self.adminSettingsFrame, text="Remove Account", command=lambda: self.remove_user())
        self.removeUserButton.grid(row=1, column=1, sticky="ew")

        self.deleteAllUserButton = CTkButton(self.adminSettingsFrame, text="Delete All User", command=lambda: print("delete all user"))

    def remove_user(self):
        selected_item = self.accountTreeview.focus()
        username = self.accountTreeview.item(selected_item, "1")
        accounts.delete_user(username)
        self.accountTreeview.delete(selected_item)

    def on_select(self):
        self.selected_item = self.accountTreeview.focus()

    def get_all_accounts(self):
        for data in accounts.get_all_accounts():
            self.accountTreeview.insert("", "end", values=data)

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
        try:
            if accounts.get_permission_level(str(accounts.get_session())):
                self.permissionLevelLabel.configure(text_color="#FF0000" ,text="ADMINISTRATOR")
            else:
                self.permissionLevelLabel.configure(text_color="#00AA00" ,text="USER ACCOUNT")
        except:
            self.permissionLevelLabel.configure(text_color="#00AA00" ,text="ACCOUNT INVALID")
