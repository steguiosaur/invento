from utils import accounts, itemdata, settings, Assets
from customtkinter import CTkFrame, set_appearance_mode, set_default_color_theme, set_widget_scaling
from tkinter import PhotoImage, Tk
from pages import *

class Main(Tk):
    def __init__(self):
        super().__init__()

        # creates container for frames
        container = CTkFrame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {} # create page dictionary
        for f in [InventoryPage, LoginPage, RegisterPage]:
            page = f.__name__
            frame = f(container, self)
            frame.grid(row=0, column=0, sticky="NSEW")
            self.frames[page] = frame

        # initialize starting frame
        self.get_session()

    # display selected page on top
    def show_frame(self, page, id=None):
        self.id = id
        self.frames[page].tkraise()

    # current logged in account
    def get_session(self):
        if accounts.get_session() is None:
            return self.show_frame("LoginPage")
        return self.show_frame("InventoryPage")

# create database and admin account if not exists
accounts.create_table()
itemdata.create_inventory_table()

# initialize settings and themes
settings.initialize_config()
set_appearance_mode(settings.appearance_read())
set_default_color_theme(settings.theme_read())
set_widget_scaling(settings.int_scale_read())

# start application
app = Main()
app.title("Invento")
app.resizable(True, True)
width = 1024
height = 576
x = (app.winfo_screenwidth()/2) - width/2
y = (app.winfo_screenheight()/2) - height/2
app.geometry('%dx%d+%d+%d' % (width, height, x, y))
app.minsize(1024, 576)
app.iconphoto(True, PhotoImage(file=Assets.asset_path('logo.png')))
app.mainloop()
