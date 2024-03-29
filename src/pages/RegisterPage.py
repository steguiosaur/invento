from customtkinter import CENTER, CTkButton, CTkEntry, CTkLabel, CTkCheckBox
from customwidget import LoginBg
from utils import accounts

class RegisterPage(LoginBg):
    def __init__(self, parent, controller):
        LoginBg.__init__(self, parent)

        # text labels
        self.registerReplyLabel = CTkLabel(self.loginFrame, anchor="nw", text="", text_color="#FF0000", font=("Roboto", 10 * -1))
        self.textLabelCreate = CTkLabel(self.loginFrame, text="Create an Account", font=('Roboto', 22))
        self.orLabel = CTkLabel(self.loginFrame, text="or", font=('Century Gothic',10))
        self.usernameReplyLabel = CTkLabel(self.loginFrame, anchor="nw", text="", text_color="#FF0000", font=("Roboto", 10 * -1))
        self.passwordReplyLabel = CTkLabel(self.loginFrame, anchor="nw", text="", text_color="#FF0000", font=("Roboto", 10 * -1))
        self.confirmPasswordReplyLabel = CTkLabel(self.loginFrame, anchor="nw", text="", text_color="#FF0000", font=("Roboto", 10 * -1))
        self.registerReplyLabel.place(relx=0.75, y=62, anchor=CENTER)
        self.textLabelCreate.place(relx=0.75, y=35, anchor=CENTER)
        self.orLabel.place(relx=0.75, y=285, anchor=CENTER)
        self.usernameReplyLabel.place(x=373, y=93)
        self.passwordReplyLabel.place(x=373, y=148)
        self.confirmPasswordReplyLabel.place(x=373, y=203)
        
        # entry for USERNAME, PASSWORD and CONFIRM PASSWORD
        self.usernameEntry = CTkEntry(self.loginFrame, width=220, placeholder_text="Username")
        self.passwordEntry = CTkEntry(self.loginFrame, width=220, placeholder_text="Password", show="*")
        self.confirmPasswordEntry = CTkEntry(self.loginFrame, width=220, placeholder_text="Confirm Password", show="*")

        self.usernameEntry.place(relx=0.75, y=80, anchor=CENTER)
        self.passwordEntry.place(relx=0.75, y=135, anchor=CENTER)
        self.confirmPasswordEntry.place(relx=0.75, y=190, anchor=CENTER)

        # BUTTONS
        # show and hide password button
        self.showPasswordCheckbox = CTkCheckBox(self.loginFrame, height=12, checkbox_width=12, checkbox_height=12, border_width=2, text="Show Password", font=('Century Gothic',10), command=lambda: self.show_hide_pass())

        # register entries on database
        self.registerInputButton = CTkButton(self.loginFrame, width=220, text="Register now", command=lambda: self.verify_registration())

        # change page to LoginPage
        self.goLoginButton = CTkButton(self.loginFrame, width=220, text="Back to Login Page", fg_color='gray', hover_color='#6F6F6F', command=lambda: self.go_login(controller))

        self.showPasswordCheckbox.place(x=373, y=220)
        self.registerInputButton.place(relx=0.75, y=260, anchor=CENTER)
        self.goLoginButton.place(relx=0.75, y=310, anchor=CENTER)


    def clear_entry(self):
        # clear existing text on entries
        self.usernameEntry.delete(0, "end")
        self.passwordEntry.delete(0, "end")
        self.confirmPasswordEntry.delete(0, "end")
        self.refresh_unfocused()
        self.reply_label_remove()


    def log_info(self, username, passwd, confirm_pass):
        # registered information status on database
        match accounts.register(username, passwd, confirm_pass):
            case 0:     # success
                self.registerReplyLabel.configure(text_color="#00AA00", text="Account registered")
            case 1:     # register failed
                self.registerReplyLabel.configure(text="Account already existed")
            case 2:     # register failed
                self.confirmPasswordReplyLabel.configure(text="*Password confirmation do not match")
            case _:     # register failed
                self.usernameReplyLabel.configure(text="*Account registration failed")


    def go_login(self, controller):
        self.clear_entry()
        controller.show_frame("LoginPage", controller.id)


    def refresh_unfocused(self):
        # refresh placeholder_text and password show to *
        self.usernameEntry.focus_set()
        self.passwordEntry.focus_set()
        self.confirmPasswordEntry.focus_set()
        self.show_hide_pass()
        self.focus_set()


    def reply_label_remove(self):
        # remove error and confirm labels
        self.usernameReplyLabel.configure(text="")
        self.passwordReplyLabel.configure(text="")
        self.confirmPasswordReplyLabel.configure(text="")
        self.registerReplyLabel.configure(text_color="#FF0000", text="")


    def show_hide_pass(self):
        if self.showPasswordCheckbox.get() == 1:
            self.passwordEntry.configure(show="")
            self.confirmPasswordEntry.configure(show="")
        else:
            self.passwordEntry.configure(show="*")
            self.confirmPasswordEntry.configure(show="*")


    def verify_registration(self):
        username, password, conf_pass = self.usernameEntry.get(), self.passwordEntry.get(), self.confirmPasswordEntry.get()
        self.clear_entry()
        if username == password == conf_pass == "":
            self.usernameReplyLabel.configure(text="*All fields are required")
            self.passwordReplyLabel.configure(text="*All fields are required")
            self.confirmPasswordReplyLabel.configure(text="*All fields are required")
            return
        if username == password == "":
            self.usernameReplyLabel.configure(text="*Username field is required")
            self.passwordReplyLabel.configure(text="*Password field is required")
            return
        if username == conf_pass == "":
            self.usernameReplyLabel.configure(text="*Username field is required")
            self.confirmPasswordReplyLabel.configure(text="*Confirm password field is required")
            return
        if password == conf_pass == "":
            self.passwordReplyLabel.configure(text="*Password field is required")
            self.confirmPasswordReplyLabel.configure(text="*Confirm password field is required")
            return
        if username == "":
            self.usernameReplyLabel.configure(text="*Username field is required")
            return
        if password == "":
            self.passwordReplyLabel.configure(text="*Password field is required")
            return
        if conf_pass == "":
            self.confirmPasswordReplyLabel.configure(text="*Confirm password field is required")
            return
        self.log_info(username, password, conf_pass)
