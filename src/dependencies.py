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
        window.configure(background="#2b2b2b")
        window.geometry("700x100")
        window.resizable(False, False)

        logoPhotoLabel = Label(window, text="invento Package Installer", fg="#DFDFDF", bg="#2b2b2b", font=("Roboto", 22))
        logoPhotoLabel.place(x=10, y=10, anchor="nw")

        textLabel = Label(window, width=600, text="This will only happen once. Internet access required\n", fg="white", bg="#2b2b2b", font=("Calibri", 8))
        textLabel.place(relx=0.5, rely=0.99, anchor="s")
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

dependency_install_window()
