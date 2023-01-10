from AccountPage import LoginPage, RegisterPage
from InventoryPage import InventoryPage
from Functionality import dependencies, accounts, settings
dependencies.dependency_install_window()
from customtkinter import CTk, CTkFrame, set_appearance_mode, set_default_color_theme, set_widget_scaling
from configparser import ConfigParser
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

# create account database if not exists
accounts.create_table()

# initialize settings and themes
settings.initialize_config()
config = ConfigParser()
config.read('config.ini')
set_appearance_mode(str(config.get('settings', 'appearance')))
set_default_color_theme(str(config.get('settings', 'theme')))
set_widget_scaling(int(config.get('settings', 'scale')) /100)

# start application
app = Main()
app.geometry(f"{1280}x{720}")
app.minsize(720, 480)
#app.maxsize(1920, 1080)
app.resizable(True, True)
app.title("Invento")

icon = PhotoImage(file='assets/logo.png')
app.iconphoto(True, icon)
app.mainloop()
