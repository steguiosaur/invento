from tkinter import Canvas, Button, Frame, PhotoImage, Entry, StringVar
from pathlib import Path

# Login page frame
class LoginPage(Frame):
    
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
    
        ############################ PRIMARY UI ############################
        # canvas for current frame
        canvas = Canvas(self, bg="#FFFFFF", height=720, width=1280, bd=0, highlightthickness=0, relief="ridge")
        canvas.place(x = 0, y = 0)

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
        canvas.create_rectangle(723.0, 115.0, 1163.0, 605.0, fill="#525249", outline="")
        
        # welcome back message on login page
        canvas.create_text(897.0, 170.0, anchor="nw", text="WELCOME BACK", fill="#D6D6D6", font=("RobotoRoman Bold", 12 * -1))
        
        # login to your account text
        self.login_to_your_account = PhotoImage(
            file=self.relative_to_assets("login_to_your_account.png"))
        canvas.create_image(943.0, 202.0, image=self.login_to_your_account)
        
        ############################# USERNAME #############################
        # username field label
        canvas.create_text( 784.0, 247.0, anchor="nw", text="Username", fill="#FFFFFF", font=("RobotoRoman Regular", 14 * -1))
        
        # username box field
        self.username_box = PhotoImage(file=self.relative_to_assets("input_box.png"))
        canvas.create_image(943.0, 290.0, image=self.username_box)
        
        # username field input
        self.username_field = Entry(
            bd=0,
            bg="#53534A",
            fg="#FFFFFF",
            highlightthickness=0
        )
        self.username_field.place(
            x=794.0,
            y=277.0,
            width=299.0,
            height=24.0
        )

        ############################# PASSWORD #############################
        self.count = 0
        self.passwd = StringVar()
        # password field label
        canvas.create_text(784.0, 345.0, anchor="nw", text="Password", fill="#FFFFFF", font=("RobotoRoman Regular", 14 * -1))
        
        # password box field
        self.password_box = PhotoImage(file=self.relative_to_assets("input_box.png"))
        canvas.create_image(943.0, 388.0, image=self.password_box)
        
        # create password input field
        self.password_field = Entry(self, textvariable=self.passwd, show="*",  bd=0, bg="#53534A", fg="#FFFFFF", highlightthickness=0)
        self.password_field.place(x=794.0, y=375.0, width=268.0, height=24.0)
        
        # hide password
        self.hide_eye = PhotoImage(
            file=self.relative_to_assets("hide_eye.png"))
        self.show_eye = PhotoImage(
            file=self.relative_to_assets("show_eye.png"))
        self.button_reveal = Button(
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

        ############################# ACCOUNTS #############################
        # login button
        self.login_now = PhotoImage(file=self.relative_to_assets("login.png"))
        button_login = Button(
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
            image=self.create_acc,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        button_acc.place(
            x=889.0,
            y=514.0,
            width=103.0,
            height=19.0
        )
        
    ############################## FUNCTIONS ###############################
    # show or hide password
    def show_hide_pass(self):
        if self.count % 2 == 0:
            self.button_reveal["image"] = self.hide_eye
            self.password_field.config(show="")
        else:
            self.button_reveal["image"] = self.show_eye
            self.password_field.config(show="*")
        self.count = 1 if self.count == 0 else 0

    # clearing entry inputs
    def clear_text(self):
        self.username_field.delete(0, 'end')
        self.password_field.delete(0, 'end')

    # reset entry background 1 border
    def reset_bg1_border(self):
        self.entryBg1.configure(image=self.imgEntry1)
        self.emailResponse.configure(text="")

    # reset entry background 2 border
    def reset_bg2_border(self):
        self.entryBg2.configure(image=self.imgEntry1)
        self.pwdResponse.configure(text="")

    # reset the entry backgrounds and entry responses
    def reset_all(self):
        self.clear_text()
        self.reset_bg1_border()
        self.reset_bg2_border()
    
    # access PATH to ASSETS_PATH
    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)
