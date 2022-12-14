from tkinter import PhotoImage, Tk, Frame
from LoginPage import LoginPage

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

        # creating a dictionary for page objects
        self.frames = {}

        # looping in every page/class and creating an object of it
        # then storing the class name as the key
        # and the object of it as the value
        for p in {LoginPage.LoginPage}:
            page_name = p.__name__
            frame = p(container, self)
            frame.grid(row=0, column=0, sticky="NSEW")
            self.frames[page_name] = frame

        self.show_frame("LoginPage")

    # showing the current frame above everything
    def show_frame(self, page_name, id=None):
        self.id = id
        frame = self.frames[page_name]
        frame.tkraise()


# initialize main window app
window = MainPage()
window.geometry("1280x720")
window.resizable(False, False)
window.title("Invento")

icon = PhotoImage(file='assets/logo.png')
window.iconphoto(True, icon)
window.mainloop()
