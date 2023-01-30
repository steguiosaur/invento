from customtkinter import CENTER, CTkFrame, CTkButton, CTkEntry, CTkLabel, CTkImage, CTkCheckBox
from pathlib import Path
from PIL import Image
from utils import accounts

class LoginPage(CTkFrame):

    # location of assets
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("../assets")

    def __init__(self, parent, controller):
        CTkFrame.__init__(self, parent)

        # background image for login
        self.bgImg = CTkImage(
            light_image=Image.open(self.asset_path("./light_bg.jpg")),
            dark_image=Image.open(self.asset_path("./dark_bg.jpg")),
            size=(1920, 1080))
        self.bgImgLabel=CTkLabel(self, image=self.bgImg, text="")
        self.bgImgLabel.pack(anchor="ne")

        # create frame for login
        self.loginFrame = CTkFrame(self, width=640, height=360, corner_radius=0)
        self.loginFrame.place(relx=0.5, rely=0.5, anchor=CENTER)

        # application logo
        self.logoImg = CTkImage(
            light_image=Image.open(self.asset_path("./light_bg_logo.png")),
            dark_image=Image.open(self.asset_path("./dark_bg_logo.png")),
            size=(264, 75))
        self.logoImgLabel=CTkLabel(self.loginFrame, image=self.logoImg, text="")
        self.logoImgLabel.place(relx=0.28, rely=0.5, anchor=CENTER)

        # labels
        self.textLabelLogin = CTkLabel(self.loginFrame, text="Log into your Account", font=('Roboto', 22))
        self.orLabel = CTkLabel(self.loginFrame, text="or", font=('Century Gothic',10))
        self.usernameReplyLabel = CTkLabel(self.loginFrame, anchor="nw", text="", text_color="#FF0F2F", font=("Roboto", 10 * -1))
        self.passwordReplyLabel = CTkLabel(self.loginFrame, anchor="nw", text="", text_color="#FF0F2F", font=("Roboto", 10 * -1))

        self.textLabelLogin.place(relx=0.75, y=45, anchor=CENTER)
        self.orLabel.place(relx=0.75, y=265, anchor=CENTER)
        self.usernameReplyLabel.place(x=373, y=123)
        self.passwordReplyLabel.place(x=373, y=178)
        
        # entry USERNAME and PASSWORD
        self.usernameEntry = CTkEntry(self.loginFrame, width=220, placeholder_text="Username")
        self.passwordEntry = CTkEntry(self.loginFrame, width=220, placeholder_text="Password", show="*")

        self.usernameEntry.place(relx=0.75, y=110, anchor=CENTER)
        self.passwordEntry.place(relx=0.75, y=165, anchor=CENTER)

        # BUTTONS
        # show and hide password button
        self.showPasswordCheckbox = CTkCheckBox(self.loginFrame, checkbox_width=12, checkbox_height=12, border_width=2, text="Show Password", font=('Century Gothic',10), command=lambda: self.show_hide_pass())

        # verify login and go to InventoryPage
        self.loginButton = CTkButton(self.loginFrame, width=220, text="Login now", command=lambda: self.verify_login(controller))

        # go to RegisterPage
        self.registerButton= CTkButton(self.loginFrame, width=220, text="Create an account", fg_color='gray', hover_color='#6F6F6F', command=lambda: self.go_register(controller))

        self.showPasswordCheckbox.place(x=373, y=193)
        self.loginButton.place(relx=0.75, y=240, anchor=CENTER)
        self.registerButton.place(relx=0.75, y=290, anchor=CENTER)

    # METHODS
    def show_hide_pass(self):
        if self.showPasswordCheckbox.get() == 1:
            self.passwordEntry.configure(show="")
        else:
            self.passwordEntry.configure(show="*")

    def verify_login(self, controller):
        username = self.usernameEntry.get()
        passwd = self.passwordEntry.get()
        self.clear_entry()
        if username == passwd == "":
            self.usernameReplyLabel.configure(text="*All fields are required")
            self.passwordReplyLabel.configure(text="*All fields are required")
            return 
        if username == "":
            self.usernameReplyLabel.configure(text="*Username field is required")
            return
        if passwd == "":
            self.passwordReplyLabel.configure(text="*Password field is required")
            return
        self.login(username, passwd, controller)

    def login(self, username, passwd, controller):
        # confirm if account is in database
        match accounts.login(username, passwd):
            case 0:
                self.go_inventory(controller)
            case 1:
                self.passwordReplyLabel.configure(text="*Incorrect password")
            case _:
                self.usernameReplyLabel.configure(text="*Account not registered")

    def go_inventory(self, controller):
        controller.show_frame("InventoryPage", controller.id)

    def go_register(self, controller):
        self.clear_entry()
        controller.show_frame("RegisterPage", controller.id)

    def refresh_unfocused(self):
        # refresh placeholder_text and password show to *
        self.usernameEntry.focus_set()
        self.passwordEntry.focus_set()
        self.show_hide_pass()
        self.focus_set()

    def reply_label_remove(self):
        # remove error and confirm labels
        self.usernameReplyLabel.configure(text="")
        self.passwordReplyLabel.configure(text="")

    def clear_entry(self):
        # clear existing text on entries
        self.usernameEntry.delete(0, 'end')
        self.passwordEntry.delete(0, 'end')
        self.refresh_unfocused()
        self.reply_label_remove()

    def asset_path(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)
