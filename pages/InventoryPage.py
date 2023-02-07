from customtkinter import CTkFrame, CTkButton, CTkLabel, CTkImage, CTkTabview 
from utils import Assets, accounts
from PIL import Image
from tabs import *

class InventoryPage(CTkFrame):
    def __init__(self, parent, controller):
        self.controller = controller
        CTkFrame.__init__(self, parent)
        self.grid_columnconfigure((0, 2, 3), weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)

        # create tabs
        self.tabview = CTkTabview(self, width=250)
        self.tabview.grid(row=0, column=1, rowspan=4, padx=(10, 10), pady=(0, 10), sticky="nsew")
        self.tabview.add("Dashboard")
        self.tabview.add("Inventory")
        self.tabview.add("Account")
        self.tabview.add("Settings")
        self.tabview.add("About")

        # create sidebar frame with widgets
        self.sidebarFrame = CTkFrame(self, width=160, corner_radius=0)
        self.sidebarFrame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebarFrame.grid_rowconfigure((1, 2, 3, 9), weight=1)

        # application logo
        self.logoImg = CTkImage(
            light_image=Image.open(Assets.asset_path("./light_bg_logo.png")),
            dark_image=Image.open(Assets.asset_path("./dark_bg_logo.png")),
            size=(170, 50))
        self.logoImgLabel=CTkLabel(self.sidebarFrame, image=self.logoImg, text="")
        self.logoImgLabel.grid(row=0, column=0, padx=20, pady=(20, 10))

        # sidebar buttons
        self.dashboardButton = CTkButton(self.sidebarFrame, text="DASHBOARD", command=lambda: self.tabview.set("Dashboard"), font=("Arial", 13, "bold"))
        self.inventoryButton = CTkButton(self.sidebarFrame, text="INVENTORY", command=lambda: self.tabview.set("Inventory"), font=("Arial", 13, "bold"))
        self.accountMenuButton = CTkButton(self.sidebarFrame, text="ACCOUNT", command=lambda: self.tabview.set("Account"), font=("Arial", 13, "bold"))
        self.settingsMenuButton = CTkButton(self.sidebarFrame, text="SETTINGS", command=lambda: self.tabview.set("Settings"), font=("Arial", 13, "bold"))
        self.aboutMenuButton = CTkButton(self.sidebarFrame, text="ABOUT", command=lambda: self.tabview.set("About"), font=("Arial", 13, "bold"))
        self.logoutButton = CTkButton(self.sidebarFrame, text="LOGOUT", fg_color="#FF0F2F", hover_color="#AF0F2F", command=lambda: self.logout(controller), font=("Arial", 13, "bold"))

        self.dashboardButton.grid(row=4, column=0, padx=20, pady=10)
        self.inventoryButton.grid(row=5, column=0, padx=20, pady=10)
        self.accountMenuButton.grid(row=6, column=0, padx=20, pady=10)
        self.settingsMenuButton.grid(row=7, column=0, padx=20, pady=10)
        self.aboutMenuButton.grid(row=8, column=0, padx=20, pady=10)
        self.logoutButton.grid(row=10, column=0, padx=20, pady=20)

        # DASHBOARD
        self.tabview.tab("Dashboard").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Dashboard").grid_rowconfigure(0, weight=1)
        self.dashboardDisplay = DashboardTab(self.tabview.tab("Dashboard"))
        self.dashboardDisplay.grid(row=0, column=0, sticky="nsew")

        # INVENTORY
        self.tabview.tab("Inventory").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Inventory").grid_rowconfigure(0, weight=1)
        self.inventoryDisplay = ProductTab(self.tabview.tab("Inventory"))
        self.inventoryDisplay.grid(row=0, column=0, sticky="nsew")

        # ACCOUNT
        self.tabview.tab("Account").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Account").grid_rowconfigure(0, weight=1)
        self.accountDisplay = AccountTab(self.tabview.tab("Account"))
        self.accountDisplay.grid(row=0, column=0, sticky="nsew")

        # ABOUTMENU
        self.tabview.tab("About").grid_columnconfigure(0, weight=1)
        self.tabview.tab("About").grid_rowconfigure(0, weight=1)
        self.aboutDisplay = AboutTab(self.tabview.tab("About"))
        self.aboutDisplay.grid(row=0, column=0, sticky="nsew")
        
        # SETTINGS
        self.tabview.tab("Settings").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Settings").grid_rowconfigure(0, weight=1)
        self.settingsDisplay = SettingsTab(self.tabview.tab("Settings"), controller)
        self.settingsDisplay.grid(row=0, column=0, sticky="nsew")


    def logout(self, controller):
        accounts.logout()   # remove account from session
        controller.show_frame("LoginPage", controller.id)
