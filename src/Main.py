from AccountPage.LoginPage import LoginPage
from AccountPage.RegisterPage import RegisterPage
from InventoryPage.InventoryPage import InventoryPage
from Functionality import dependencies, accounts, settings
dependencies.dependency_install_window()
from customtkinter import CTk, CTkFrame, set_appearance_mode, set_default_color_theme, set_widget_scaling
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
        for f in {LoginPage, RegisterPage, InventoryPage}:
            page = f.__name__
            frame = f(container, self)
            frame.grid(row=0, column=0, sticky="NSEW")
            self.frames[page] = frame

        # initialize starting frame
        self.show_frame("LoginPage")

    # display selected page on top
    def show_frame(self, page, id=None):
        self.id = id
        frame = self.frames[page]
        frame.tkraise()

# create account database and admin account if not exists
accounts.create_table()

# initialize settings and themes
settings.initialize_config()
set_appearance_mode(settings.appearance_read())
set_default_color_theme(settings.theme_read())
set_widget_scaling(settings.int_scale_read())

# start application
app = Main()
app.geometry(f"{1024}x{576}")
app.minsize(1024, 576)
app.resizable(True, True)
app.iconphoto(True, PhotoImage(file='assets/logo.png'))
app.title("Invento")
app.mainloop()
