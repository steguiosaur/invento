from tkinter import Frame, Canvas, Entry, Button, PhotoImage
from pathlib import Path

class ShowInventory(Frame):

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"./assets")
        
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        
        ############################ PRIMARY UI ############################
        canvas = Canvas(self, bg = "#FFFFFF", height=720, width=1280, bd=0, highlightthickness=0, relief = "ridge")
        canvas.place(x=0, y=0)

        canvas.create_rectangle(0.0, 37.0, 295.0, 720.0, fill="#D6D6D6", outline="")
        
        canvas.create_rectangle(0.0, 0.0, 1280.0, 37.0, fill="#5B5B5B", outline="")
        
        canvas.create_rectangle(295.0, 37.0, 1280.0, 148.0, fill="#B8B8B8", outline="")
        
        canvas.create_rectangle(295.0, 148.0, 672.0, 175.0, fill="#A7A7A7", outline="")
        
        canvas.create_rectangle(672.0, 148.0, 823.0, 175.0, fill="#A7A7A7", outline="")
        
        canvas.create_rectangle(823.0, 148.0, 976.0, 175.0, fill="#A7A7A7", outline="")
        
        canvas.create_rectangle(976.0, 148.0, 1135.0, 175.0, fill="#A7A7A7", outline="")
        
        canvas.create_rectangle(1135.0, 148.0, 1280.0, 175.0, fill="#A7A7A7", outline="")
        
        ############################ SEARCH UI #############################
        self.searchBg = PhotoImage(
            file=self.relative_to_assets("searchBg.png"))
        canvas.create_image(491.0, 90.0, image=self.searchBg)
        
        ########################### PRODUCT NAME ############################
        self.productNameBox = PhotoImage(
            file=self.relative_to_assets("productNameBox.png"))
        canvas.create_image(147.0, 195.0, image=self.productNameBox)
        
        entry_1 = Entry(
            self,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        entry_1.place(
            x=34.0,
            y=182.0,
            width=226.0,
            height=24.0
        )
        
        self.entry_image_2 = PhotoImage(
            file=self.relative_to_assets("entry_2.png"))
        canvas.create_image(
            506.0,
            90.5,
            image=self.entry_image_2
        )
        entry_2 = Entry(
            self,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        entry_2.place(
            x=392.0,
            y=77.0,
            width=228.0,
            height=25.0
        )
        
        self.button_image_1 = PhotoImage(
            file=self.relative_to_assets("button_1.png"))
        button_1 = Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        button_1.place(
            x=672.0,
            y=72.0,
            width=109.0,
            height=36.0
        )
        
        self.button_image_2 = PhotoImage(
            file=self.relative_to_assets("button_2.png"))
        button_2 = Button(
            self,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        button_2.place(
            x=23.0,
            y=661.0,
            width=244.0,
            height=36.0
        )
        
        self.button_image_3 = PhotoImage(
            file=self.relative_to_assets("button_3.png"))
        button_3 = Button(
            self,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        button_3.place(
            x=23.0,
            y=350.0,
            width=244.0,
            height=36.0
        )
        
        self.button_image_4 = PhotoImage(
            file=self.relative_to_assets("button_4.png"))
        button_4 = Button(
            self,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
            relief="flat"
        )
        button_4.place(
            x=23.0,
            y=403.0,
            width=244.0,
            height=36.0
        )
        
        canvas.create_text(
            113.0,
            702.0,
            anchor="nw",
            text="Ver 0.0.221215",
            fill="#545454",
            font=("RobotoRoman Regular", 10 * -1)
        )
        
        self.image_image_3 = PhotoImage(
            file=self.relative_to_assets("image_3.png"))
        canvas.create_image(
            159.0,
            97.0,
            image=self.image_image_3
        )
        
        canvas.create_text(
            23.0,
            159.0,
            anchor="nw",
            text="Product Name",
            fill="#2B2B2B",
            font=("RobotoRoman Medium", 12 * -1)
        )
        
        self.image_image_4 = PhotoImage(
            file=self.relative_to_assets("image_4.png"))
        canvas.create_image(
            80.0,
            254.0,
            image=self.image_image_4
        )
        
        self.entry_image_3 = PhotoImage(
            file=self.relative_to_assets("entry_3.png"))
        canvas.create_image(
            79.5,
            254.0,
            image=self.entry_image_3
        )
        entry_3 = Entry(
            self,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        entry_3.place(
            x=34.0,
            y=241.0,
            width=91.0,
            height=24.0
        )
        
        self.image_image_5 = PhotoImage(
            file=self.relative_to_assets("image_5.png"))
        canvas.create_image(
            208.0,
            255.0,
            image=self.image_image_5
        )
        
        self.entry_image_4 = PhotoImage(
            file=self.relative_to_assets("entry_4.png"))
        canvas.create_image(
            208.0,
            255.0,
            image=self.entry_image_4
        )
        entry_4 = Entry(
            self,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        entry_4.place(
            x=159.0,
            y=242.0,
            width=98.0,
            height=24.0
        )
        
        canvas.create_text(
            23.0,
            218.0,
            anchor="nw",
            text="Required Stock",
            fill="#2B2B2B",
            font=("RobotoRoman Medium", 12 * -1)
        )
        
        canvas.create_text(
            150.0,
            218.0,
            anchor="nw",
            text="Current Stock",
            fill="#2B2B2B",
            font=("RobotoRoman Medium", 12 * -1)
        )
        
        self.image_image_6 = PhotoImage(
            file=self.relative_to_assets("image_6.png"))
        canvas.create_image(
            80.0,
            314.0,
            image=self.image_image_6
        )
        
        self.entry_image_5 = PhotoImage(
            file=self.relative_to_assets("entry_5.png"))
        canvas.create_image(
            79.5,
            314.0,
            image=self.entry_image_5
        )
        entry_5 = Entry(
            self,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        entry_5.place(
            x=34.0,
            y=301.0,
            width=91.0,
            height=24.0
        )
        
        self.image_image_7 = PhotoImage(
            file=self.relative_to_assets("image_7.png"))
        canvas.create_image(
            208.0,
            315.0,
            image=self.image_image_7
        )
        
        self.entry_image_6 = PhotoImage(
            file=self.relative_to_assets("entry_6.png"))
        canvas.create_image(
            208.0,
            315.0,
            image=self.entry_image_6
        )
        entry_6 = Entry(
            self,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        entry_6.place(
            x=159.0,
            y=302.0,
            width=98.0,
            height=24.0
        )
        
        canvas.create_text(
            23.0,
            278.0,
            anchor="nw",
            text="Market Price",
            fill="#2B2B2B",
            font=("RobotoRoman Medium", 12 * -1)
        )
        
        canvas.create_text(
            150.0,
            278.0,
            anchor="nw",
            text="Selling Price",
            fill="#2B2B2B",
            font=("RobotoRoman Medium", 12 * -1)
        )
        
        canvas.create_rectangle(
            671.0,
            147.0,
            672.0,
            720.0,
            fill="#3B3B3B",
            outline="")
        
        canvas.create_rectangle(
            975.0,
            147.0,
            976.0,
            720.0,
            fill="#3B3B3B",
            outline="")
        
        canvas.create_rectangle(
            1134.0,
            147.0,
            1135.0,
            720.0,
            fill="#3B3B3B",
            outline="")
        
        canvas.create_rectangle(
            822.0,
            147.0,
            823.0,
            720.0,
            fill="#3B3B3B",
            outline="")
        
        canvas.create_text(
            303.0,
            152.0,
            anchor="nw",
            text="Product Name",
            fill="#2B2B2B",
            font=("RobotoRoman Medium", 15 * -1)
        )
        
        canvas.create_text(
            678.0,
            152.0,
            anchor="nw",
            text="Current Stock",
            fill="#2B2B2B",
            font=("RobotoRoman Medium", 15 * -1)
        )
        
        canvas.create_text(
            831.0,
            152.0,
            anchor="nw",
            text="Required Stock",
            fill="#2B2B2B",
            font=("RobotoRoman Medium", 15 * -1)
        )
        
        canvas.create_text(
            984.0,
            152.0,
            anchor="nw",
            text="Market Price",
            fill="#2B2B2B",
            font=("RobotoRoman Medium", 15 * -1)
        )
        
        canvas.create_text(
            1143.0,
            152.0,
            anchor="nw",
            text="Selling Price",
            fill="#2B2B2B",
            font=("RobotoRoman Medium", 15 * -1)
        )
            
    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)
