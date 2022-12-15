from tkinter import Canvas, Button, Frame, PhotoImage, Entry, StringVar, Label
from pathlib import Path
import accounts

# Login page frame
class LoginPage(Frame):
    
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
    
        ############################ PRIMARY UI ############################
        # canvas for current frame
        canvas = Canvas(self, bg="#D6D6D6", height=720, width=1280, bd=0, highlightthickness=0, relief="ridge")
        canvas.place(x=0, y=0)

        # create background display
        self.book_bg = PhotoImage(file=self.relative_to_assets("book_bg.png"))
        canvas.create_image(643.0, 360.0, image=self.book_bg)
        
        # create logo
        self.logo = PhotoImage(file=self.relative_to_assets("logo.png"))
        canvas.create_image(205.0, 355.0, image=self.logo)
        
        # create application name
        self.invento = PhotoImage(file=self.relative_to_assets("invento.png"))
        canvas.create_image(398.0, 366.0, image=self.invento)
        
        # create login field background
        self.rectangle = PhotoImage(file=self.relative_to_assets("fill_rectangle.png"))
        canvas.create_image(943.0, 360.0, image=self.rectangle)
        
        # welcome back message on login page
        canvas.create_text(897.0, 170.0, anchor="nw", text="WELCOME BACK", fill="#D6D6D6", font=("RobotoRoman Bold", 12 * -1))
        
        # login to your account text
        self.login_to_your_account = PhotoImage(
            file=self.relative_to_assets("login_to_your_account.png"))
        canvas.create_image(943.0, 202.0, image=self.login_to_your_account)
        
        # error box
        self.errorBox = PhotoImage(file=self.relative_to_assets("error_box.png"))
        ############################# USERNAME #############################
        self.username = StringVar()
        self.username.trace("w", self.redo_username_action)
        # username field label
        canvas.create_text( 784.0, 247.0, anchor="nw", text="Username", fill="#FFFFFF", font=("RobotoRoman Regular", 14 * -1))
        
        # username box
        self.username_box = PhotoImage(file=self.relative_to_assets("input_box.png"))
        canvas.create_image(943.0, 290.0, image=self.username_box)
        
        # username field input
        self.username_bg = Label(self, image=self.username_box)
        #self.username_bg.place(x=943.0 ,y=290.0, anchor=CENTER)
        self.username_field = Entry(self, textvariable=self.username, bd=0, bg="#53534A", fg="#FFFFFF", highlightthickness=0)
        self.username_field.place(x=794.0, y=277.0, width=299.0, height=24.0)
        
        self.user_field_reply = Label(canvas, anchor="nw", bg="#53534A", fg="#9D0404", font=("Inter", 10 * -1))
        self.user_field_reply.place(x=990.0, y=250.0)

        ############################# PASSWORD #############################
        self.count = 0
        self.passwd = StringVar()
        self.passwd.trace("w", self.redo_passwd_action)
        # password field label
        canvas.create_text(784.0, 345.0, anchor="nw", text="Password", fill="#FFFFFF", font=("RobotoRoman Regular", 14 * -1))
        
        # password box
        self.password_box = PhotoImage(file=self.relative_to_assets("input_box.png"))
        canvas.create_image(943.0, 388.0, image=self.password_box)
        
        # create password input field
        self.password_bg = Label(self, image=self.password_box)
        #self.password_bg.place(x=943.0, y=388.0, anchor=CENTER)
        self.password_field = Entry(self, textvariable=self.passwd, show="*",  bd=0, bg="#53534A", fg="#FFFFFF", highlightthickness=0)
        self.password_field.place(x=794.0, y=375.0, width=268.0, height=24.0)
        
        # hide password
        self.hide_eye = PhotoImage(
            file=self.relative_to_assets("hide_eye.png"))
        self.show_eye = PhotoImage(
            file=self.relative_to_assets("show_eye.png"))
        self.button_reveal = Button(
            self,
            image=self.show_eye,
            borderwidth=0,
            highlightthickness=0,
            command=self.show_hide_pass,
            relief="flat"
        )
        self.button_reveal.place(
            x=1064.0,
            y=378.0,
            width=22.0,
            height=22.0
        )

        self.pass_field_reply = Label(canvas, anchor="nw", bg="#53534A", fg="#9D0404", font=("Inter", 10 * -1))
        self.pass_field_reply.place(x=990.0, y=348.0)
        ############################# ACCOUNTS #############################
        # login button
        self.login_now = PhotoImage(file=self.relative_to_assets("login.png"))
        button_login = Button(
            self,
            image=self.login_now,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.inventory_login(controller),
            relief="flat"
        )
        button_login.place(
            x=784.0,
            y=458.0,
            width=318.0,
            height=45.0
        )
        
        # not registered question label
        canvas.create_text(784.0, 516.0, anchor="nw", text="Not registered yet?", fill="#D6D6D6", font=("RobotoRoman Regular", 12 * -1))
        
        # create account button
        self.create_acc = PhotoImage(file=self.relative_to_assets("create_acc.png"))
        button_acc = Button(
            self,
            image=self.create_acc,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.go_register(controller),
            relief="flat"
        )
        button_acc.place(
            x=889.0,
            y=514.0,
            width=103.0,
            height=19.0
        )
        
    ############################## FUNCTIONS ###############################
    # Register page
    def go_register(self, controller):
        self.reset_all()
        controller.show_frame("RegisterPage", controller.id)

    # show or hide password
    def show_hide_pass(self):
        if self.count % 2 == 0:
            self.button_reveal["image"] = self.hide_eye
            self.password_field.config(show="")
        else:
            self.button_reveal["image"] = self.show_eye
            self.password_field.config(show="*")
        self.count = 1 if self.count == 0 else 0

    # transition to the right menu
    def inventory_login(self, controller):
        username = self.username_field.get()
        passwd = self.password_field.get()
        self.clear_text()

        # if email and password is both empty
        if username == passwd == "":
            self.user_field_reply["text"] = self.pass_field_reply["text"] = "*All fields are required*"
            #self.username_box["image"] = self.password_box["image"] = self.errorBox
            return 

        # if email is empty
        if username == "":
            self.user_field_reply["text"] = "Username field is required"
            #self.password_box["image"] = self.errorBox
            return

        # if password is empty
        if passwd == "":
            self.pass_field_reply["text"] = "Password field is required"
            #self.username_box["image"] = self.errorBox
            return

        self.login(username, passwd, controller)

    def login(self, username, passwd, controller):
        login_status = accounts.login(username, passwd)

        match login_status:
            case 0:
                #inventorydb.Database()
                controller.show_frame("ShowInventory")
            case 1:
                self.pass_field_reply["text"]="Incorrect password"
                #self.password_bg['image']=self.errorBox
            case _:
                self.user_field_reply["text"] = "Account not registered"
                #self.username_bg['image']=self.errorBox

    # clearing entry inputs
    def clear_text(self):
        self.username_field.delete(0, 'end')
        self.password_field.delete(0, 'end')

    # reset entry background 1 border
    def redo_username_action(self, *args):
        #self.username_bg.configure(image=self.username_box)
        self.user_field_reply.configure(text="")

    # reset entry background 2 border
    def redo_passwd_action(self, *args):
        #self.password_bg.configure(image=self.password_box)
        self.pass_field_reply.configure(text="")

    # reset the entry backgrounds and entry responses
    def reset_all(self):
        self.clear_text()
        self.redo_username_action()
        self.redo_passwd_action()

    # access PATH to ASSETS_PATH
    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)
