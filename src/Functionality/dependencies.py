from tkinter import CENTER, Tk, Label, PhotoImage
from os.path import isfile
from pathlib import Path
import subprocess

packages = [
    "customtkinter",
    "pillow",
    "pandas"
]

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("../assets")


def dependency_install_window():
    if not isfile('./account.db'):
        window = Tk()
        window.configure(background="#1b1b1b")
        window.geometry("489x301")
        window.resizable(False, False)
        window.title("Invento Dependency Installer")

        icon = PhotoImage(file=relative_to_assets('logo.png'))
        window.iconphoto(True, icon)

        bgInstaller = PhotoImage(file=relative_to_assets("dependency_installer.png"))
        bgIntallerLabel = Label(window, image=bgInstaller)
        bgIntallerLabel.pack()

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

        textLabel["text"] = "Finished Loading\n"
        window.after(2000, window.update())
        window.destroy()

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
