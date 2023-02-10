from customtkinter import CENTER, CTkButton, CTkEntry, CTkLabel, CTkCheckBox
from customwidget import LoginBg
from utils import accounts

class LoginPage(LoginBg):
    def __init__(self, parent, controller):
        self.controller = controller
        LoginBg.__init__(self, parent)

        # text labels
        self.textLabelLogin = CTkLabel(self.loginFrame, text="Log into your Account", font=('Roboto', 22))
        self.orLabel = CTkLabel(self.loginFrame, text="or", font=('Century Gothic',10))
        self.usernameReplyLabel = CTkLabel(self.loginFrame, anchor="nw", text="", text_color="#FF0000", font=("Roboto", 10 * -1))
        self.passwordReplyLabel = CTkLabel(self.loginFrame, anchor="nw", text="", text_color="#FF0000", font=("Roboto", 10 * -1))
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
        self.showPasswordCheckbox.place(x=373, y=193)

        # verify login, change page to InventoryPage
        self.loginButton = CTkButton(self.loginFrame, width=220, text="Login now", command=lambda: self.verify_login(controller))
        self.loginButton.place(relx=0.75, y=240, anchor=CENTER)

        # change page to RegisterPage
        self.registerButton= CTkButton(self.loginFrame, width=220, text="Create an account", fg_color='gray', hover_color='#6F6F6F', command=lambda: self.go_register(controller))
        self.registerButton.place(relx=0.75, y=290, anchor=CENTER)


    def clear_entry(self):
        # clear existing text on entries
        self.usernameEntry.delete(0, 'end')
        self.passwordEntry.delete(0, 'end')
        self.refresh_unfocused()
        self.reply_label_remove()


    def go_inventory(self, controller):
        controller.show_frame("InventoryPage", controller.id)


    def go_register(self, controller):
        self.clear_entry()
        controller.show_frame("RegisterPage", controller.id)


    def login(self, username, passwd, controller):
        match accounts.login(username, passwd):
            case 0:     # logged in
                self.controller.frames["InventoryPage"].accountDisplay.refresh_account()
                self.controller.frames["InventoryPage"].dashboardDisplay.reload_all()
                self.go_inventory(controller)
            case 1:     # login fail
                self.passwordReplyLabel.configure(text="*Incorrect password")
            case _:     # login fail
                self.usernameReplyLabel.configure(text="*Account not registered")


    def refresh_unfocused(self):
        # refresh placeholder_text and password show to *
        self.usernameEntry.focus_set()
        self.passwordEntry.focus_set()
        self.show_hide_pass()
        self.focus_set()


    def reply_label_remove(self):
        self.usernameReplyLabel.configure(text="")
        self.passwordReplyLabel.configure(text="")


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
