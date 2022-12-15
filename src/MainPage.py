from tkinter import PhotoImage, Tk, Frame
from LoginPage import LoginPage
from RegisterPage import RegisterPage
from ShowInventory import ShowInventory

class MainPage(Tk):
    # init method of the class MainFrame
    def __init__(self, *args, **kwargs):
        # init method of the tk class
        Tk.__init__(self, *args, **kwargs)

        # creating a container for all
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # object frames dictionary 
        self.frames = {}

        # change frame
        for f in {LoginPage.LoginPage, RegisterPage.RegisterPage, ShowInventory.ShowInventory}:
            page_name = f.__name__
            frame = f(container, self)
            frame.grid(row=0, column=0, sticky="NSEW")
            self.frames[page_name] = frame

        self.show_frame("LoginPage")

    # hold selected frame
    def show_frame(self, page_name, id=None):
        self.id = id
        frame = self.frames[page_name]
        frame.tkraise()


# create main window
main = MainPage()
main.geometry("1280x720")
main.resizable(False, False)
main.title("Invento")

icon = PhotoImage(file='assets/logo.png')
main.iconphoto(True, icon)
main.mainloop()
