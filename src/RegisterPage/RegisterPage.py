from tkinter import Frame, Canvas, Entry, Button, PhotoImage
from pathlib import Path


class RegisterPage(Frame):
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")
        
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        canvas = Canvas(self, bg = "#FFFFFF", height = 720, width = 1280, bd=0, highlightthickness = 0, relief = "ridge")
        canvas.place(x=0, y=0)

        self.book_bg = PhotoImage(
            file=self.relative_to_assets("book_bg.png"))
        canvas.create_image(
            643.0,
            360.0,
            image=self.book_bg
        )
        
        image_image_2 = PhotoImage(
            file=self.relative_to_assets("image_2.png"))
        image_2 = canvas.create_image(
            205.0,
            355.0,
            image=image_image_2
        )
        
        image_image_3 = PhotoImage(
            file=self.relative_to_assets("image_3.png"))
        image_3 = canvas.create_image(
            398.0,
            366.0,
            image=image_image_3
        )
        
        image_image_4 = PhotoImage(
            file=self.relative_to_assets("image_4.png"))
        image_4 = canvas.create_image(
            943.0,
            360.0,
            image=image_image_4
        )
        
        entry_image_1 = PhotoImage(
            file=self.relative_to_assets("entry_1.png"))
        entry_bg_1 = canvas.create_image(
            922.5,
            326.0,
            image=entry_image_1
        )
        entry_1 = Entry(
            bd=0,
            bg="#53534A",
            fg="#000716",
            highlightthickness=0
        )
        entry_1.place(
            x=794.0,
            y=313.0,
            width=257.0,
            height=24.0
        )
        
        image_image_5 = PhotoImage(
            file=self.relative_to_assets("image_5.png"))
        image_5 = canvas.create_image(
            943.0,
            228.0,
            image=image_image_5
        )
        
        canvas.create_text(
            784.0,
            185.0,
            anchor="nw",
            text="Username",
            fill="#FFFFFF",
            font=("RobotoRoman Regular", 14 * -1)
        )
        
        image_image_6 = PhotoImage(
            file=self.relative_to_assets("image_6.png"))
        image_6 = canvas.create_image(
            943.0,
            326.0,
            image=image_image_6
        )
        
        button_image_1 = PhotoImage(
            file=self.relative_to_assets("button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        button_1.place(
            x=784.0,
            y=500.0,
            width=318.0,
            height=45.0
        )
        
        canvas.create_text(
            784.0,
            283.0,
            anchor="nw",
            text="Password",
            fill="#FFFFFF",
            font=("RobotoRoman Regular", 14 * -1)
        )
        
        image_image_7 = PhotoImage(
            file=self.relative_to_assets("image_7.png"))
        image_7 = canvas.create_image(
            942.0,
            161.0,
            image=image_image_7
        )
        
        entry_image_2 = PhotoImage(
            file=self.relative_to_assets("entry_2.png"))
        entry_bg_2 = canvas.create_image(
            943.5,
            228.0,
            image=entry_image_2
        )
        entry_2 = Entry(
            bd=0,
            bg="#53534A",
            fg="#000716",
            highlightthickness=0
        )
        entry_2.place(
            x=794.0,
            y=215.0,
            width=299.0,
            height=24.0
        )
        
        button_image_2 = PhotoImage(
            file=self.relative_to_assets("button_2.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        button_2.place(
            x=1064.0,
            y=316.0,
            width=22.0,
            height=22.0
        )
        
        button_image_3 = PhotoImage(
            file=self.relative_to_assets("button_3.png"))
        button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        button_3.place(
            x=1064.0,
            y=316.0,
            width=22.0,
            height=22.0
        )
        
        entry_image_3 = PhotoImage(
            file=self.relative_to_assets("entry_3.png"))
        entry_bg_3 = canvas.create_image(
            922.5,
            426.0,
            image=entry_image_3
        )
        entry_3 = Entry(
            bd=0,
            bg="#53534A",
            fg="#000716",
            highlightthickness=0
        )
        entry_3.place(
            x=794.0,
            y=413.0,
            width=257.0,
            height=24.0
        )
        
        image_image_8 = PhotoImage(
            file=self.relative_to_assets("image_8.png"))
        image_8 = canvas.create_image(
            943.0,
            426.0,
            image=image_image_8
        )
        
        canvas.create_text(
            784.0,
            383.0,
            anchor="nw",
            text="Confirm Password",
            fill="#FFFFFF",
            font=("RobotoRoman Regular", 14 * -1)
        )
        
        button_image_4 = PhotoImage(
            file=self.relative_to_assets("button_4.png"))
        button_4 = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
            relief="flat"
        )
        button_4.place(
            x=1064.0,
            y=416.0,
            width=22.0,
            height=22.0
        )
        
        button_image_5 = PhotoImage(
            file=self.relative_to_assets("button_5.png"))
        button_5 = Button(
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_5 clicked"),
            relief="flat"
        )
        button_5.place(
            x=1064.0,
            y=416.0,
            width=22.0,
            height=22.0
        )
        
        button_image_6 = PhotoImage(
            file=self.relative_to_assets("button_6.png"))
        button_6 = Button(
            image=button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_6 clicked"),
            relief="flat"
        )
        button_6.place(
            x=728.0,
            y=119.0,
            width=47.0,
            height=24.0
        )

    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)
