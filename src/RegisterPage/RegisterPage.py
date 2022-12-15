from tkinter import Frame, Canvas, Entry, Button, PhotoImage, StringVar
from pathlib import Path
import accounts


class RegisterPage(Frame):
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        ############################ PRIMARY UI ############################
        canvas = Canvas(self, bg = "#D6D6D6", height = 720, width = 1280, bd=0, highlightthickness = 0, relief = "ridge")
        canvas.place(x=0, y=0)

        # backgound image
        self.book_bg = PhotoImage(file=self.relative_to_assets("book_bg.png"))
        canvas.create_image(643.0, 360.0, image=self.book_bg)
        
        self.logo = PhotoImage(file=self.relative_to_assets("logo.png"))
        canvas.create_image(205.0, 355.0, image=self.logo)
        
        self.invento = PhotoImage(file=self.relative_to_assets("invento.png"))
        canvas.create_image(398.0, 366.0, image=self.invento)
        
        self.rectangle = PhotoImage(file=self.relative_to_assets("fill_rectangle.png"))
        canvas.create_image(943.0, 360.0, image=self.rectangle)

        self.register_title = PhotoImage(file=self.relative_to_assets("register_title.png"))
        canvas.create_image(942.0, 161.0, image=self.register_title)
        
        ############################# USERNAME #############################
        self.username = StringVar()
        #self.username.trace("w", self.redo_username_action)

        canvas.create_text(784.0, 185.0, anchor="nw", text="Username", fill="#FFFFFF", font=("RobotoRoman Regular", 14 * -1))
        
        self.username_box = PhotoImage(file=self.relative_to_assets("entry_field.png"))
        canvas.create_image(943.0, 228.0, image=self.username_box)
        
        self.user_entry = Entry(self, textvariable=self.username ,bd=0, bg="#53534A", fg="#FFFFFF", highlightthickness=0)
        self.user_entry.place(x=794.0, y=215.0, width=299.0, height=24.0)
        
        ############################# PASSWORD #############################
        self.count = 0
        self.passwd = StringVar()
        #self.passwd.trace("w", self.redo_passwd_action)
        canvas.create_text(784.0, 283.0, anchor="nw", text="Password", fill="#FFFFFF", font=("RobotoRoman Regular", 14 * -1))
        
        self.password_box = PhotoImage(file=self.relative_to_assets("entry_field.png"))
        canvas.create_image(943.0, 326.0, image=self.password_box)

        self.password_entry = Entry(self, textvariable=self.passwd, show="*",bd=0, bg="#53534A", fg="#FFFFFF", highlightthickness=0)
        self.password_entry.place(x=794.0, y=313.0, width=257.0, height=24.0)
        
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
        self.button_reveal.place(x=1064.0, y=316.0, width=22.0, height=22.0)

        ############################# CONFIRMP #############################
        self.confirmp = StringVar()
        canvas.create_text(784.0, 383.0, anchor="nw", text="Confirm Password", fill="#FFFFFF", font=("RobotoRoman Regular", 14 * -1))

        self.confirm_pass_box = PhotoImage(
            file=self.relative_to_assets("entry_field.png"))
        canvas.create_image(943.0, 426.0, image=self.confirm_pass_box)


        self.confirm_pass_field = Entry(
            self,
            textvariable=self.confirmp,
            show="*",
            bd=0,
            bg="#53534A",
            fg="#FFFFFF",
            highlightthickness=0
        )
        self.confirm_pass_field.place(x=794.0, y=413.0, width=257.0, height=24.0)
        
        self.button_reveal_conf = Button(
            self,
            image=self.show_eye,
            borderwidth=0,
            highlightthickness=0,
            command=self.show_hide_pass,
            relief="flat"
        )
        self.button_reveal_conf.place(
            x=1064.0,
            y=416.0,
            width=22.0,
            height=22.0
        )
        
        ############################# ACCOUNTS #############################
        self.register_box = PhotoImage(
            file=self.relative_to_assets("register.png"))
        self.register_button = Button(
            self,
            image=self.register_box,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.read_input(controller),
            relief="flat"
        )
        self.register_button.place(x=784.0, y=500.0, width=318.0, height=45.0)
        
        self.back_login = PhotoImage(
            file=self.relative_to_assets("back_login.png"))
        login_button = Button(
            self,
            image=self.back_login,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.go_login(controller),
            relief="flat"
        )
        login_button.place(x=728.0, y=119.0, width=47.0, height=24.0)

    ############################## FUNCTIONS ###############################
    def go_login(self, controller):
        self.reset_all()
        controller.show_frame("LoginPage", controller.id)
    # show or hide password
    def show_hide_pass(self):
        if self.count % 2 == 0:
            self.button_reveal["image"] = self.hide_eye
            self.password_entry.config(show="")
            self.button_reveal_conf["image"] = self.hide_eye
            self.confirm_pass_field.config(show="")
        else:
            self.button_reveal["image"] = self.show_eye
            self.password_entry.config(show="*")
            self.button_reveal_conf["image"] = self.show_eye
            self.confirm_pass_field.config(show="*")
        self.count = 1 if self.count == 0 else 0

    # creating an account
    def read_input(self, controller):
        username, password, conf_pass = self.user_entry.get(), self.password_entry.get(), self.confirm_pass_field.get()
        self.clear_text()

        # if email, password, and confirm password are all empty
        if username == password == conf_pass == "":
            return

        # if email only is empty
        if username == "":
            return

        # both password and confirm password are empty
        if password == conf_pass == "":
            return

        self.log_info(username, password, conf_pass)

    def log_info(self, username, passwd, confirm_pass):
        accounts.register(username, passwd, confirm_pass)

    # clearing entry inputs
    def clear_text(self):
        #self.response.place_forget()
        self.user_entry.delete(0, "end")
        self.password_entry.delete(0, "end")
        self.confirm_pass_field.delete(0, "end")


    # reset entry background 1 border
#    def reset_bg1_border(self, *args):
#        #self.entryBg1.configure(image=self.imgEntry1)
#        #self.emailResponse.configure(text="")
#
#
#    # reset entry background 2 border
#    def reset_bg2_border(self, *args):
#        #self.entryBg2.configure(image=self.imgEntry1)
#        #self.pwdResponse.configure(text="")
#
#
#    # reset entry background 3 border
#    def reset_bg3_border(self, *args):
#        #self.entryBg3.configure(image=self.imgEntry1)
#        #self.confirmResponse.configure(text="")


    # reset the entry backgrounds and entry responses
    def reset_all(self):
        self.clear_text()
        #self.reset_bg1_border()
        #self.reset_bg2_border()
        #self.reset_bg3_border()



    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)
