from tkinter import Frame, Canvas, Entry, Button, PhotoImage, StringVar, IntVar, Label
from pathlib import Path
import sqlite3

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
        
        canvas.create_text(113.0, 702.0, anchor="nw", text="Ver 0.0.221215", fill="#545454", font=("RobotoRoman Regular", 10 * -1))

        self.image_image_3 = PhotoImage(file=self.relative_to_assets("image_3.png"))
        canvas.create_image(159.0, 97.0, image=self.image_image_3)
        
        self.image_image_4 = PhotoImage(file=self.relative_to_assets("image_4.png"))
        canvas.create_image(80.0, 254.0, image=self.image_image_4)
        
        self.image_image_5 = PhotoImage(file=self.relative_to_assets("image_5.png"))
        canvas.create_image(208.0, 255.0, image=self.image_image_5)
        
        self.image_image_6 = PhotoImage(file=self.relative_to_assets("image_6.png"))
        canvas.create_image(80.0, 314.0, image=self.image_image_6)
        
        self.image_image_7 = PhotoImage(file=self.relative_to_assets("image_7.png"))
        canvas.create_image(208.0, 315.0, image=self.image_image_7)
        
        ############################ SEARCH UI #############################
        self.search = StringVar()
        self.searchBg = PhotoImage(
            file=self.relative_to_assets("searchBg.png"))
        canvas.create_image(491.0, 90.0, image=self.searchBg)
        
        self.searchEntry = Entry(
            self,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.searchEntry.place(x=392.0, y=77.0, width=228.0, height=25.0)
        
        self.searchButtonImg = PhotoImage(
            file=self.relative_to_assets("searchButton.png"))
        self.searchButton = Button(
            self,
            textvariable=self.search,
            image=self.searchButtonImg,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        self.searchButton.place(x=672.0, y=72.0, width=109.0, height=36.0)

        ########################### PRODUCT NAME ############################
        self.productName = StringVar()
        self.productNameBox = PhotoImage(
            file=self.relative_to_assets("productNameBox.png"))
        canvas.create_image(147.0, 195.0, image=self.productNameBox)
        
        self.productNameEntry = Entry(
            self,
            textvariable=self.productName,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.productNameEntry.place(x=34.0, y=182.0, width=226.0, height=24.0)
        
        ########################### REQUIRE STK ############################
        self.requireStock = IntVar()
        self.requiredStockEntry = Entry(
            self,
            textvariable=self.requireStock,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.requiredStockEntry.place(x=34.0, y=241.0, width=91.0, height=24.0)

        ########################### CURRENT STK ############################
        self.currentStock = IntVar()
        self.currentStockEntry = Entry(
            self,
            textvariable=self.currentStock,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.currentStockEntry.place(x=159.0, y=242.0, width=98.0, height=24.0)
        
        ########################### MARKET PRICE ############################
        self.marketPrice = IntVar()
        self.marketPriceEntry = Entry(
            self,
            textvariable=self.marketPrice,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.marketPriceEntry.place(x=34.0, y=301.0, width=91.0, height=24.0)

        ########################### SELLING PRICE ###########################
        self.sellingPrice = IntVar()
        self.sellingPriceEntry = Entry(
            self,
            textvariable=self.sellingPrice,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.sellingPriceEntry.place(x=159.0, y=302.0, width=98.0, height=24.0)
        
        ############################# ACCOUNT ##############################
        self.logoutButtonImg = PhotoImage(
            file=self.relative_to_assets("logout.png"))
        self.logoutButton = Button(
            self,
            image=self.logoutButtonImg,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.go_login,
            relief="flat"
        )
        self.logoutButton.place(x=23.0, y=661.0, width=244.0, height=36.0)
        
        ###################### BUTTON TO DATABASE ###########################
        self.addButtonImg = PhotoImage(
            file=self.relative_to_assets("add.png"))
        self.addButton = Button(
            self,
            image=self.addButtonImg,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.add_product,
            relief="flat"
        )
        self.addButton.place(x=23.0, y=350.0, width=244.0, height=36.0)
        
        self.deleteButtonImg = PhotoImage(
            file=self.relative_to_assets("delete.png"))
        self.deleteButton = Button(
            self,
            image=self.deleteButtonImg,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
            relief="flat"
        )
        self.deleteButton.place(x=23.0, y=403.0, width=244.0, height=36.0)
        
        ####################################################################
        canvas.create_text(23.0, 159.0, anchor="nw", text="Product Name", fill="#2B2B2B", font=("RobotoRoman Medium", 12 * -1))
        
        canvas.create_text(23.0, 218.0, anchor="nw", text="Required Stock", fill="#2B2B2B", font=("RobotoRoman Medium", 12 * -1))
        
        canvas.create_text(150.0, 218.0, anchor="nw", text="Current Stock", fill="#2B2B2B", font=("RobotoRoman Medium", 12 * -1))
        
        canvas.create_text(23.0, 278.0, anchor="nw", text="Market Price", fill="#2B2B2B", font=("RobotoRoman Medium", 12 * -1))
        
        canvas.create_text(150.0, 278.0, anchor="nw", text="Selling Price", fill="#2B2B2B", font=("RobotoRoman Medium", 12 * -1))
        
        canvas.create_rectangle(671.0, 147.0, 672.0, 720.0, fill="#3B3B3B", outline="")
        
        canvas.create_rectangle(975.0, 147.0, 976.0, 720.0, fill="#3B3B3B", outline="")
        
        canvas.create_rectangle(1134.0, 147.0, 1135.0, 720.0, fill="#3B3B3B", outline="")
        
        canvas.create_rectangle(822.0, 147.0, 823.0, 720.0, fill="#3B3B3B", outline="")
        
        canvas.create_text(303.0, 152.0, anchor="nw", text="Product Name", fill="#2B2B2B", font=("RobotoRoman Medium", 15 * -1))
        
        canvas.create_text(678.0, 152.0, anchor="nw", text="Current Stock", fill="#2B2B2B", font=("RobotoRoman Medium", 15 * -1))
        
        canvas.create_text(831.0, 152.0, anchor="nw", text="Required Stock", fill="#2B2B2B", font=("RobotoRoman Medium", 15 * -1))
        
        canvas.create_text(984.0, 152.0, anchor="nw", text="Market Price", fill="#2B2B2B", font=("RobotoRoman Medium", 15 * -1))
        
        canvas.create_text(1143.0, 152.0, anchor="nw", text="Selling Price", fill="#2B2B2B", font=("RobotoRoman Medium", 15 * -1))
            

    ############################## testing grounds ###############################
        #hide preset data list
        #self.frame_display = Frame(self, bg="#FFFFFF")
        #self.frame_display.place(x=295.0,y=148.0,width=1280.0,height=720.0)
       # self.frame_display = PhotoImage(file=self.relative_to_assets("image_8.png"))
       # self.frame_label = Label(self, image=self.frame_display)
       # self.frame_label.place(x=295.0, y=148.0, width=1280.0, height=720.0)
        # coordinate
        #canvas.create_rectangle(295.0,148.0,1280.0,720.0,fill="#FFFFFF",outline="")
    ############################## FUNCTIONS ###############################
    # return to login [NEED FIX]
    def go_login(self, controller):
        self.reset_all()
        controller.show_frame("LoginPage", controller.id)

    ############################## DATABASE ###############################
    # Create database on first login
    def Database(self):
        global conn, cursor
        conn = sqlite3.connect("inventory.db")
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS `product` (product_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Product_Name TEXT, Required_Stock TEXT, Current_Stock TEXT, Market_Price TEXT, Selling_Price TEXT)")

    def AddNew(self, productName, requiredStock, currentStock, marketPrice, sellingPrice):
        self.Database()
        cursor.execute("INSERT INTO `product` (Product_Name, Required_Stock, Current_Stock, Market_Price, Selling_Price) VALUES(?, ?, ?, ?, ?)", (str(productName.get()),int(requiredStock.get()), int(currentStock.get()), int(marketPrice.get()), int(sellingPrice.get())))
        conn.commit()
        cursor.close()
        conn.close()

    def add_product(self, productName, currentStock, requireStock, marketPrice, sellingPrice):
        self.AddNew(productName, currentStock, requireStock, marketPrice, sellingPrice)
    
    def display_table(self):
        self.Database()
        r_set=conn.execute('''SELECT * from product LIMIT 0,10''');
        i=0 # row value inside the loop 
        for product in r_set: 
            for j in range(len(product)):
                e = Entry(self, width=10, fg='blue') 
                e.grid(row=i, column=j) 
                e.insert('end', product[j])
            i=i+1
        
    ############################## FUNCTIONS ###############################
    # clearing search inputs
    def clear_search(self):
        self.searchEntry.delete(0, 'end')

    # clearing entry inputs
    def clear_text(self):
        self.productNameEntry.delete(0, 'end')
        self.requiredStockEntry.delete(0, 'end')
        self.currentStockEntry.delete(0, 'end')
        self.marketPriceEntry.delete(0, 'end')
        self.sellingPriceEntry.delete(0, 'end')

    # reset the entry backgrounds and entry responses
    def reset_all(self):
        self.clear_search()
        self.clear_text()

    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)
