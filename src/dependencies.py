from tkinter import Tk, Label, PhotoImage
from os.path import isfile
import subprocess

packages = [
    "customtkinter",
    "pillow",
    "pandas"
]

def dependency_install_window():
    if not isfile('./account.db'):
        window = Tk()
        window.configure(background="#1b1b1b")
        window.geometry("700x100")
        window.resizable(False, False)
        window.title("Invento Dependency Installer")

        icon = PhotoImage(file='assets/logo.png')
        window.iconphoto(True, icon)

        logoPhotoLabel = Label(window, text="INVENTO dependency installer", fg="#DFDFDF", bg="#1b1b1b", font=("Georgia", 16))
        logoPhotoLabel.place(x=5, y=0, anchor="nw")

        textLabel = Label(window, width=600, text="Connecting...", fg="white", bg="#2b2b2b", font=("Calibri", 8))
        textLabel.place(relx=0.5, rely=0.98, anchor="s")

        textLabel2 = Label(window, width=600, text="This only happen once. Internet access required.", fg="white", bg="#1b1b1b", font=("Calibri", 8))
        textLabel2.place(relx=0.5, rely=1, anchor="s")
        window.update()

        # import or install required dependencies
        for package in range(0, len(packages)):
            textLabel["text"] = ""
            process = subprocess.Popen(["pip", "install", packages[package]], stdout=subprocess.PIPE)
            output, _ = process.communicate()
            output = output.decode()
            textLabel["text"] = output
            window.update()

        textLabel["text"] = "Finished Loading\n"
        window.after(2000, window.update())
        window.destroy()

#dependency_install_window()
