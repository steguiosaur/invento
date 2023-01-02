import customtkinter
from AccountPage import LoginPage, RegisterPage
from InventoryPage import InventoryPage
from customtkinter import CTk, CTkFrame

class Main(CTk):
    def __init__(self, *args, **kwargs):
        CTk.__init__(self, *args, **kwargs)

        container = CTkFrame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for f in {
            LoginPage.LoginPage, 
            RegisterPage.RegisterPage, 
            InventoryPage.InventoryPage
        }:
            page = f.__name__
            frame = f(container, self)
            frame.grid(row=0, column=0, sticky="NSEW")
            self.frames[page] = frame

        self.show_frame("LoginPage")

    def show_frame(self, page, id=None):
        self.id = id
        frame = self.frames[page]
        frame.tkraise()

customtkinter.set_appearance_mode("dark")
app = Main()
app.geometry(f"{1280}x{720}")
app.minsize(720, 480)
app.resizable(True, True)
app.title("Invento")

app.mainloop()
