from AccountPage import LoginPage, RegisterPage
from InventoryPage import InventoryPage
import dependencies
dependencies.dependency_install()
from customtkinter import CTk, CTkFrame, set_appearance_mode
from tkinter import PhotoImage

class Main(CTk):
    def __init__(self, *args, **kwargs):
        CTk.__init__(self, *args, **kwargs)

        # creates container for frames
        container = CTkFrame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # create dictionary 
        self.frames = {}

        # application pages  
        for f in {
            LoginPage.LoginPage, 
            RegisterPage.RegisterPage, 
            InventoryPage.InventoryPage
        }:
            page = f.__name__
            frame = f(container, self)
            frame.grid(row=0, column=0, sticky="NSEW")
            self.frames[page] = frame

        # initialize starting frame
        self.show_frame("LoginPage")

    def show_frame(self, page, id=None):
        self.id = id
        frame = self.frames[page]
        frame.tkraise()

set_appearance_mode("dark")
app = Main()
app.geometry(f"{1280}x{720}")
app.minsize(720, 480)
app.resizable(True, True)
app.title("Invento")

icon = PhotoImage(file='assets/logo.png')
app.iconphoto(True, icon)
app.mainloop()
