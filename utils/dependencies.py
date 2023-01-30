from tkinter import Tk, Label, PhotoImage
from os.path import isfile
from pathlib import Path
import subprocess

# required packages
packages = [
    "customtkinter",
    "pillow"
]

# location of assets
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("../assets")

# window for installing dependencies
def dependency_install_window():
    # executes installer on first startup
    if not isfile('./config.ini'):
        window = Tk()
        window.configure(background="#1b1b1b")
        window.geometry("489x301")
        window.resizable(False, False)
        window.title("Invento Dependency Installer")
        icon = PhotoImage(file=relative_to_assets('logo.png'))
        window.iconphoto(True, icon)

        # image for installer
        bgInstaller = PhotoImage(file=relative_to_assets("dependency_installer.png"))
        bgIntallerLabel = Label(window, image=bgInstaller)
        bgIntallerLabel.pack()

        # display installation texts
        textLabel = Label(window, width=600, text="Connecting...", fg="white", bg="#2b2b2b", font=("Calibri", 7))
        textLabel.place(relx=0.5, rely=1, anchor="s")
        window.update()

        # import or install required dependencies
        for package in range(0, len(packages)):
            textLabel["text"] = ""
            process = subprocess.Popen(["pip", "install", packages[package]], stdout=subprocess.PIPE)
            output, _ = process.communicate()
            output = output.decode()
            textLabel["text"] = output
            window.update()

        # close window after install
        textLabel["text"] = "Finished Loading\n"
        window.after(2000, window.update())
        window.destroy()

# path of assets
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
