from customtkinter import CENTER, CTkFrame, CTkButton, CTkEntry, CTkLabel, CTkImage, CTkCheckBox
from pathlib import Path
from PIL import Image
from Functionality import accounts

class RegisterPage(CTkFrame):

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("../assets")

    def __init__(self, parent, controller):
        CTkFrame.__init__(self, parent)

        ############################ PRIMARY UI ############################
        # Background image FIX [Transparency, Size]
        self.bgImg = CTkImage(
            light_image=Image.open(self.asset_path("./light_bg.jpg")),
            dark_image=Image.open(self.asset_path("./dark_bg.jpg")),
            size=(1920, 1080))
        
        self.bgImgLabel=CTkLabel(self, image=self.bgImg, text="")
        self.bgImgLabel.pack()

        ######################### REGISTER FRAME
        self.registerFrame = CTkFrame(self, width=640, height=360, corner_radius=0)
        self.registerFrame.place(relx=0.5, rely=0.5, anchor=CENTER)

        # application logo
        self.logoImg = CTkImage(
            light_image=Image.open(self.asset_path("./light_bg_logo.png")),
            dark_image=Image.open(self.asset_path("./dark_bg_logo.png")),
            size=(264, 75))
        self.logoImgLabel=CTkLabel(self.registerFrame, image=self.logoImg, text="")
        self.logoImgLabel.place(relx=0.28, rely=0.5, anchor=CENTER)

        # labels
        self.registerReplyLabel = CTkLabel(self.registerFrame, anchor="nw", text="", text_color="#FF0F2F", font=("Roboto", 10 * -1))
        self.registerReplyLabel.place(relx=0.75, y=62, anchor=CENTER)

        self.textLabelCreate = CTkLabel(self.registerFrame, text="Create an Account", font=('Roboto', 22))
        self.textLabelCreate.place(relx=0.75, y=35, anchor=CENTER)

        self.orLabel = CTkLabel(self.registerFrame, text="or", font=('Century Gothic',10))
        self.orLabel.place(relx=0.75, y=285, anchor=CENTER)
        
        ############################ USERNAME
        self.usernameReplyLabel = CTkLabel(self.registerFrame, anchor="nw", text="", text_color="#FF0F2F", font=("Roboto", 10 * -1))
        self.usernameReplyLabel.place(x=373, y=93)

        self.usernameEntry = CTkEntry(self.registerFrame, width=220, placeholder_text="Username")
        self.usernameEntry.place(relx=0.75, y=80, anchor=CENTER)

        ############################ PASSWORD
        self.passwordReplyLabel = CTkLabel(self.registerFrame, anchor="nw", text="", text_color="#FF0F2F", font=("Roboto", 10 * -1))
        self.passwordReplyLabel.place(x=373, y=148)

        self.passwordEntry = CTkEntry(self.registerFrame, width=220, placeholder_text="Password", show="*")
        self.passwordEntry.place(relx=0.75, y=135, anchor=CENTER)

        ######################## CONFIRM PASSWORD
        self.confirmPasswordReplyLabel = CTkLabel(self.registerFrame, anchor="nw", text="", text_color="#FF0F2F", font=("Roboto", 10 * -1))
        self.confirmPasswordReplyLabel.place(x=373, y=203)

        self.confirmPasswordEntry = CTkEntry(self.registerFrame, width=220, placeholder_text="Confirm Password", show="*")
        self.confirmPasswordEntry.place(relx=0.75, y=190, anchor=CENTER)

        ############################ BUTTONS
        # show and hide password button
        self.showPasswordCheckbox = CTkCheckBox(self.registerFrame, height=12, checkbox_width=12, checkbox_height=12, border_width=2, text="Show Password", font=('Century Gothic',10), command=lambda: self.show_hide_pass())
        self.showPasswordCheckbox.place(x=373, y=220)

        # register entries to database
        self.registerInputButton = CTkButton(self.registerFrame, width=220, text="Register now", command=lambda: self.verify_registration())
        self.registerInputButton.place(relx=0.75, y=260, anchor=CENTER)

        # return to LoginPage
        self.goLoginButton = CTkButton(self.registerFrame, width=220, text="Back to Login Page", fg_color='gray', hover_color='#6F6F6F', command=lambda: self.go_login(controller))
        self.goLoginButton.place(relx=0.75, y=310, anchor=CENTER)

    ############################## FUNCTIONS ###############################
    # shows and hides password
    def show_hide_pass(self):
        boxValue = self.showPasswordCheckbox.get()
        if boxValue == 1:
            self.passwordEntry.configure(show="")
            self.confirmPasswordEntry.configure(show="")
        else:
            self.passwordEntry.configure(show="*")
            self.confirmPasswordEntry.configure(show="*")

    # verify entry to account database
    def verify_registration(self):
        username, password, conf_pass = self.usernameEntry.get(), self.passwordEntry.get(), self.confirmPasswordEntry.get()
        self.clear_entry()
        # if email, password, and confirm password are all empty
        if username == password == conf_pass == "":
            self.usernameReplyLabel.configure(text="*All fields are required")
            self.passwordReplyLabel.configure(text="*All fields are required")
            self.confirmPasswordReplyLabel.configure(text="*All fields are required")
            return
        # both username and password are empty
        if username == password == "":
            self.usernameReplyLabel.configure(text="*Username field is required")
            self.passwordReplyLabel.configure(text="*Password field is required")
            return
        # both username and confirm password are empty
        if username == conf_pass == "":
            self.usernameReplyLabel.configure(text="*Username field is required")
            self.confirmPasswordReplyLabel.configure(text="*Confirm password field is required")
            return
        # both password and confirm password are empty
        if password == conf_pass == "":
            self.passwordReplyLabel.configure(text="*Password field is required")
            self.confirmPasswordReplyLabel.configure(text="*Confirm password field is required")
            return
        # if username is empty
        if username == "":
            self.usernameReplyLabel.configure(text="*Username field is required")
            return
        # if password is empty
        if password == "":
            self.passwordReplyLabel.configure(text="*Password field is required")
            return
        # if confirm password is empty
        if conf_pass == "":
            self.confirmPasswordReplyLabel.configure(text="*Confirm password field is required")
            return
        # store information to account database
        self.log_info(username, password, conf_pass)

    def log_info(self, username, passwd, confirm_pass):
        login_status = accounts.register(username, passwd, confirm_pass)
        match login_status:
            case 0:
                self.registerReplyLabel.configure(text_color="#0FFF2F", text="Account registered")
            case 1:
                self.registerReplyLabel.configure(text="Account already existed")
            case 2:
                self.confirmPasswordReplyLabel.configure(text="*Password confirmation do not match")
            case _:
                self.usernameReplyLabel.configure(text="*Account not registered")

    # LoginPage frame
    def go_login(self, controller):
        self.clear_entry()
        controller.show_frame("LoginPage", controller.id)

    # refresh placeholder_text and password show to *
    def refresh_unfocused(self):
        self.usernameEntry.focus_set()
        self.passwordEntry.focus_set()
        self.confirmPasswordEntry.focus_set()
        self.show_hide_pass()
        self.focus_set()

    # remove error and confirm labels
    def reply_label_remove(self):
        self.usernameReplyLabel.configure(text="")
        self.passwordReplyLabel.configure(text="")
        self.confirmPasswordReplyLabel.configure(text="")
        self.registerReplyLabel.configure(text_color="#FF0F2F", text="")

    # clear existing text on entries
    def clear_entry(self):
        self.usernameEntry.delete(0, "end")
        self.passwordEntry.delete(0, "end")
        self.confirmPasswordEntry.delete(0, "end")
        self.refresh_unfocused()
        self.reply_label_remove()

    # path of assets
    def asset_path(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)
