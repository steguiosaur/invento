from customtkinter import CTkButton, CTkFrame, CTkImage, CTkLabel, CTkEntry, CTkCheckBox
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

        # frame for changing CURRENT PASSWORD
        self.accountConfigFrame = CTkFrame(self.accountSettingsFrame)
        self.accountConfigFrame.grid(row=5, column=0, rowspan=2, columnspan=3, padx=10, pady=(10, 5), sticky="nsew")
        self.accountConfigFrame.grid_columnconfigure(0, weight=1)
        self.accountConfigFrame.grid_columnconfigure(1, weight=1)
        self.accountConfigFrame.grid_columnconfigure(2, weight=1)
        self.accountConfigFrame.grid_columnconfigure(3, weight=1)
        self.accountConfigFrame.grid_columnconfigure(4, weight=1)
        self.accountConfigFrame.grid_rowconfigure(0, weight=0)
        self.accountConfigFrame.grid_rowconfigure(1, weight=1)
        self.accountConfigFrame.grid_rowconfigure(2, weight=0)
        self.accountConfigFrame.grid_rowconfigure(3, weight=0)
        self.accountConfigFrame.grid_rowconfigure(4, weight=0)
        self.accountConfigFrame.grid_rowconfigure(5, weight=0)
        self.accountConfigFrame.grid_rowconfigure(6, weight=0)
        self.accountConfigFrame.grid_rowconfigure(7, weight=1)
        self.accountConfigFrame.grid_rowconfigure(8, weight=1)
        self.accountConfigFrame.grid_rowconfigure(9, weight=1)

        self.accountSettingsLabel = CTkLabel(self.accountConfigFrame, text="ACCOUNT SETTINGS", font=("Arial", 13, "bold"))
        self.accountSettingsLabel.grid(row=0, column=0, columnspan=5, padx=(5, 5), sticky="")

        self.changePasswordStatusLabel = CTkLabel(self.accountConfigFrame, text="")
        self.changePasswordStatusLabel.grid(row=1, column=0, columnspan=5, sticky="")

        self.changePasswordLabel = CTkLabel(self.accountConfigFrame, text="Change Password:")
        self.changePasswordLabel.grid(row=2, column=1, padx=(5, 5), pady=5, sticky="")

        self.currentPasswordEntry = CTkEntry(self.accountConfigFrame, show="*", placeholder_text="Current Password")
        self.currentPasswordEntry.grid(row=2, column=3, pady=5, sticky="ew")
        
        self.newPasswordEntry = CTkEntry(self.accountConfigFrame, show="*", placeholder_text="New Password")
        self.newPasswordEntry.grid(row=3, column=3, pady=5, sticky="ew")

        self.confirmNewPasswordEntry = CTkEntry(self.accountConfigFrame, show="*", placeholder_text="Confirm New Password")
        self.confirmNewPasswordEntry.grid(row=4, column=3, pady=5, sticky="ew")

        self.showPasswordCheckbox = CTkCheckBox(self.accountConfigFrame, checkbox_width=12, checkbox_height=12, border_width=2, text="Show Password", font=('Century Gothic',10), command=lambda: self.show_hide_pass())
        self.showPasswordCheckbox.grid(row=5, column=3, padx=(5, 5), pady=5, sticky="w")

        self.savePasswordButton = CTkButton(self.accountConfigFrame, text="Save Password", command=lambda: self.verify_new_pass())
        self.savePasswordButton.grid(row=6, column=1, pady=5, sticky="ew")

        self.cancelNewPasswordButton = CTkButton(self.accountConfigFrame, text="Cancel", fg_color="#FF0F2F", hover_color="#AF0F2F", command=lambda: self.clear_entry())
        self.cancelNewPasswordButton.grid(row=6, column=3, pady=5, sticky="ew")

        # sensitive account settings
        self.sensitiveFrame = CTkFrame(self.accountSettingsFrame)
        self.sensitiveFrame.grid(row=7, column=0, rowspan=3, columnspan=5, padx=10, pady=(5, 10), sticky="nsew")
        self.sensitiveFrame.grid_columnconfigure(0, weight=1)
        self.sensitiveFrame.grid_columnconfigure(1, weight=1)
        self.sensitiveFrame.grid_columnconfigure(2, weight=1)
        self.sensitiveFrame.grid_columnconfigure(3, weight=1)
        self.sensitiveFrame.grid_columnconfigure(4, weight=1)
        self.sensitiveFrame.grid_rowconfigure(0, weight=1)

        self.deleteAccountButton = CTkButton(self.sensitiveFrame, text="Delete Account", fg_color="#FF0F2F", hover_color="#AF0F2F", command=lambda: self.delete_account())
        self.deleteAccountButton.grid(row=0, column=1, pady=5, sticky="ew")

        self.removeAdminButton = CTkButton(self.sensitiveFrame, text="Change to User", fg_color="#FF0F2F", hover_color="#AF0F2F", command=lambda: self.remove_admin_privilege(accounts.get_session()))
        self.removeAdminButton.grid(row=0, column=3, pady=5, sticky="ew")

        # frame for listing accounts
        self.accountListFrame = CTkFrame(self)
        self.accountListFrame.grid(row=0, column=2, rowspan=2, columnspan=2, padx=(5, 10), pady=(10, 5), sticky="nsew")
        self.accountListFrame.grid_columnconfigure(0, weight=1)
        self.accountListFrame.grid_rowconfigure(0, weight=0)
        self.accountListFrame.grid_rowconfigure(1, weight=0)
        self.accountListFrame.grid_rowconfigure(2, weight=0)
        self.accountListFrame.grid_rowconfigure(3, weight=1)

        self.accountList = CTkLabel(self.accountListFrame, text="ACCOUNT LIST", font=("Arial", 13, "bold"))
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

        # all ADMINISTRATOR required actions
        self.adminSettingsFrame = CTkFrame(self)
        self.adminSettingsFrame.grid(row=2, column=2, rowspan=2, columnspan=2, padx=(5, 10), pady=(5, 10), sticky="nsew")
        self.adminSettingsFrame.grid_columnconfigure(0, weight=1)
        self.adminSettingsFrame.grid_columnconfigure(1, weight=1)
        self.adminSettingsFrame.grid_columnconfigure(2, weight=1)
        self.adminSettingsFrame.grid_rowconfigure(0, weight=0)
        self.adminSettingsFrame.grid_rowconfigure(1, weight=0)
        self.adminSettingsFrame.grid_rowconfigure(2, weight=1)
        self.adminSettingsFrame.grid_rowconfigure(3, weight=1)
        self.adminSettingsFrame.grid_rowconfigure(4, weight=1)
        self.adminSettingsFrame.grid_rowconfigure(5, weight=1)
        self.adminSettingsFrame.grid_rowconfigure(6, weight=1)

        self.adminSettingsLabel = CTkLabel(self.adminSettingsFrame, text="ADMINISTRATOR SETTINGS", font=("Arial", 13, "bold"))
        self.adminSettingsLabel.grid(row=0, column=0, columnspan=3, sticky="")

        self.adminUserRequiredLabel = CTkLabel(self.adminSettingsFrame, text="")
        self.adminUserRequiredLabel.grid(row=1, column=0, columnspan=3, sticky="ew")

        self.grantAdminPrivilegesButton = CTkButton(self.adminSettingsFrame, text="Grant Admin Privileges", command=lambda: self.give_admin())
        self.grantAdminPrivilegesButton.grid(row=2, column=1, sticky="ew")

        self.removeAdminPrivilegesButton = CTkButton(self.adminSettingsFrame, text="Remove Admin Privileges", command=lambda: self.remove_admin_privilege_admin())
        self.removeAdminPrivilegesButton.grid(row=3, column=1, sticky="ew")

        self.removeUserButton = CTkButton(self.adminSettingsFrame, text="Remove Account", command=lambda: self.remove_user())
        self.removeUserButton.grid(row=4, column=1, sticky="ew")

        self.deleteAllUserButton = CTkButton(self.adminSettingsFrame, text="Delete All User", command=lambda: self.delete_all_user())
        self.deleteAllUserButton.grid(row=5, column=1, sticky="ew")


    def verify_new_pass(self):
        current, new_pass, conf_pass = self.currentPasswordEntry.get(), self.newPasswordEntry.get(), self.confirmNewPasswordEntry.get()
        self.clear_entry()
        if current == new_pass == conf_pass == "":
            self.changePasswordStatusLabel.configure(text="*All fields are required", text_color="#FF0000")
            return
        if current == new_pass == "":
            self.changePasswordStatusLabel.configure(text="Current and new password required", text_color="#FF0000")
            return
        if current == conf_pass == "":
            self.changePasswordStatusLabel.configure(text="*Current and confirm password required", text_color="#FF0000")
            return
        if new_pass == conf_pass == "":
            self.changePasswordStatusLabel.configure(text="*New password and confirm password required", text_color="#FF0000")
            return
        if current == "":
            self.changePasswordStatusLabel.configure(text="*Current password required", text_color="#FF0000")
            return
        if new_pass == "":
            self.changePasswordStatusLabel.configure(text="*New password required", text_color="#FF0000")
            return
        if conf_pass == "":
            self.changePasswordStatusLabel.configure(text="Confirm password required", text_color="#FF0000")
            return
        self.update_pass(current, new_pass, conf_pass)

    def update_pass(self, current, new_pass, confirm_pass):
        # registered account status on database
        match accounts.change_pass(self.show_current_session(), current, new_pass, confirm_pass):
            case 0:
                self.changePasswordStatusLabel.configure(text_color="#00AA00", text="*Password changed successfully")
                self.remove_entry_text()
            case 1:
                self.changePasswordStatusLabel.configure(text="*Password incorrect", text_color="#FF0000")
            case 2:
                self.changePasswordStatusLabel.configure(text="*Password confirmation do not match", text_color="#FF0000")
            case _:
                self.changePasswordStatusLabel.configure(text="*Password not changed", text_color="#FF0000")

    def reload_treeview(self):
        self.accountTable.change_theme(settings.table_theme_read())

    def refresh_unfocused(self):
        # refresh placeholder_text and password show to *
        self.currentPasswordEntry.focus_set()
        self.newPasswordEntry.focus_set()
        self.currentPasswordEntry.focus_set()
        self.show_hide_pass()
        self.focus_set()

    def reply_label_remove(self):
        # remove error and confirm labels
        self.changePasswordStatusLabel.configure(text="")

    def remove_entry_text(self):
        self.currentPasswordEntry.delete(0, 'end')
        self.newPasswordEntry.delete(0, 'end')
        self.confirmNewPasswordEntry.delete(0, 'end')
        self.refresh_unfocused()

    def clear_entry(self):
        # clear existing text on entries
        self.remove_entry_text()
        self.reply_label_remove()

    def delete_account(self):
        accounts.delete_user(accounts.get_session())
        self.get_all_accounts()

    def remove_admin_privilege_admin(self):
        selected_item = self.accountTreeview.focus()
        if selected_item == "":
            self.adminUserRequiredLabel.configure(text="*No account selected.", text_color="#FF0000")
            return
        selected_values = self.accountTreeview.item(selected_item)["values"]
        username = selected_values[0]
        try:
            if accounts.get_permission_level(str(accounts.get_session())):
                accounts.remove_admin_privilege(username)
                self.accountTreeview.delete(selected_item)
                self.get_all_accounts()
                self.adminUserRequiredLabel.configure(text="*Admin privileges removed.", text_color="#00AA00")
            else:
                self.adminUserRequiredLabel.configure(text="*Admin permission required.", text_color="#FF0000")
        except:
            self.adminUserRequiredLabel.configure(text="*Exception generated.", text_color="#FF0000")

    def remove_admin_privilege(self, username):
        accounts.remove_admin_privilege(username)
        self.show_permission_level()
        self.get_all_accounts()

    def show_hide_pass(self):
        if self.showPasswordCheckbox.get() == 1:
            self.currentPasswordEntry.configure(show="")
            self.newPasswordEntry.configure(show="")
            self.confirmNewPasswordEntry.configure(show="")
        else:
            self.currentPasswordEntry.configure(show="*")
            self.newPasswordEntry.configure(show="*")
            self.confirmNewPasswordEntry.configure(show="*")

    def give_admin(self):
        selected_item = self.accountTreeview.focus()
        if selected_item == "":
            self.adminUserRequiredLabel.configure(text="*No account selected.", text_color="#FF0000")
            return
        selected_values = self.accountTreeview.item(selected_item)["values"]
        username = selected_values[0]
        try:
            if accounts.get_permission_level(str(accounts.get_session())):
                accounts.grant_admin_privilege(username)
                self.accountTreeview.delete(selected_item)
                self.get_all_accounts()
                self.adminUserRequiredLabel.configure(text="*Admin privileges granted.", text_color="#00AA00")
            else:
                self.adminUserRequiredLabel.configure(text="*Admin permission required.", text_color="#FF0000")
        except:
            self.adminUserRequiredLabel.configure(text="*Exception generated.", text_color="#FF0000")

    def remove_user(self):
        selected_item = self.accountTreeview.focus()
        if selected_item == "":
            self.adminUserRequiredLabel.configure(text="*No account selected.", text_color="#FF0000")
            return
        selected_values = self.accountTreeview.item(selected_item)["values"]
        username = selected_values[0]
        try:
            if accounts.get_permission_level(str(accounts.get_session())):
                accounts.delete_user(username)
                self.accountTreeview.delete(selected_item)
                self.adminUserRequiredLabel.configure(text="*Account deleted.", text_color="#00AA00")
            else:
                self.adminUserRequiredLabel.configure(text="*Admin permission required.", text_color="#FF0000")
        except:
            self.adminUserRequiredLabel.configure(text="*Exception generated.", text_color="#FF0000")

    def delete_all_user(self):
        try:
            if accounts.get_permission_level(str(accounts.get_session())):
                accounts.delete_all_users()
                self.get_all_accounts()
                self.adminUserRequiredLabel.configure(text="*All user accounts deleted.", text_color="#00AA00")
            else:
                self.adminUserRequiredLabel.configure(text="*Admin permission required.", text_color="#FF0000")
        except:
            self.adminUserRequiredLabel.configure(text="*Exception generated.", text_color="#FF0000")

    def get_all_accounts(self):
        self.accountTreeview.delete(*self.accountTreeview.get_children())
        for data in accounts.get_all_accounts():
            self.accountTreeview.insert("", "end", values=data)

    def show_current_session(self):
        return str(accounts.get_session())

    def refresh_account(self):
        self.accountNameLabel.configure(text=self.show_current_session())
        self.refresh_picture()
        self.show_permission_level()
        self.get_all_accounts()

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
