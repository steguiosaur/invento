from customtkinter import CTkFrame, CTkButton, CTkLabel, CTkImage, CTkTabview 
from TabPages import AboutTab, SettingsTab, AccountTab, DashboardTab, ProductTab
from pathlib import Path
from PIL import Image

class InventoryPage(CTkFrame):

    # location of assets
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("../assets")

    def __init__(self, parent, controller):
        CTkFrame.__init__(self, parent)

        # configure grid layout (4x4)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=0)
        self.grid_columnconfigure(3, weight=0)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)

        ############################ CONTROL ############################
        # create tabs
        self.tabview = CTkTabview(self, width=250)
        self.tabview.grid(row=0, column=1, rowspan=4, padx=(10, 10), pady=(10, 10), sticky="nsew")
        self.tabview.add("Dashboard")
        self.tabview.add("Inventory")
        self.tabview.add("Account")
        self.tabview.add("Settings")
        self.tabview.add("About")

        # create sidebar frame with widgets
        self.sidebarFrame = CTkFrame(self, width=160, corner_radius=0)
        self.sidebarFrame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebarFrame.grid_rowconfigure(1, weight=1)
        self.sidebarFrame.grid_rowconfigure(2, weight=1)
        self.sidebarFrame.grid_rowconfigure(3, weight=1)
        self.sidebarFrame.grid_rowconfigure(9, weight=1)

        # application logo
        self.logoImg = CTkImage(
            light_image=Image.open(self.asset_path("./light_bg_logo.png")),
            dark_image=Image.open(self.asset_path("./dark_bg_logo.png")),
            size=(170, 50))
        self.logoImgLabel=CTkLabel(self.sidebarFrame, image=self.logoImg, text="")
        self.logoImgLabel.grid(row=0, column=0, padx=20, pady=(20, 10))

        # button for tabs
        self.dashboardButton = CTkButton(self.sidebarFrame, text="Dashboard", command=lambda: self.tabview.set("Dashboard"))
        self.dashboardButton.grid(row=4, column=0, padx=20, pady=10)

        self.inventoryButton = CTkButton(self.sidebarFrame, text="Inventory", command=lambda: self.tabview.set("Inventory"))
        self.inventoryButton.grid(row=5, column=0, padx=20, pady=10)

        self.accountMenuButton = CTkButton(self.sidebarFrame, text="Account", command=lambda: self.tabview.set("Account"))
        self.accountMenuButton.grid(row=6, column=0, padx=20, pady=10)

        self.settingsMenuButton = CTkButton(self.sidebarFrame, text="Settings", command=lambda: self.tabview.set("Settings"))
        self.settingsMenuButton.grid(row=7, column=0, padx=20, pady=10)

        self.aboutMenuButton = CTkButton(self.sidebarFrame, text="About", command=lambda: self.tabview.set("About"))
        self.aboutMenuButton.grid(row=8, column=0, padx=20, pady=10)

        self.logoutButton = CTkButton(self.sidebarFrame, text="Logout", command=lambda: self.logout(controller))
        self.logoutButton.grid(row=10, column=0, padx=20, pady=20)

        ############################ DASHBOARD
        self.tabview.tab("Dashboard").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Dashboard").grid_rowconfigure(0, weight=1)
        self.dashboardDisplay = DashboardTab.DashboardTab(self.tabview.tab("Dashboard"))
        self.dashboardDisplay.grid(row=0, column=0, sticky="nsew")

        ############################ INVENTORY
        self.tabview.tab("Inventory").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Inventory").grid_rowconfigure(0, weight=1)
        self.inventoryDisplay = ProductTab.ProductTab(self.tabview.tab("Inventory"))
        self.inventoryDisplay.grid(row=0, column=0, sticky="nsew")

        ############################# ACCOUNT
        self.tabview.tab("Account").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Account").grid_rowconfigure(0, weight=1)
        self.accountDisplay = AccountTab.AccountTab(self.tabview.tab("Account"))
        self.accountDisplay.grid(row=0, column=0, sticky="nsew")

        ############################ ABOUTMENU
        self.tabview.tab("About").grid_columnconfigure(0, weight=1)
        self.tabview.tab("About").grid_rowconfigure(0, weight=1)
        self.aboutDisplay = AboutTab.AboutTab(self.tabview.tab("About"))
        self.aboutDisplay.grid(row=0, column=0, sticky="nsew")
        
        ############################# SETTINGS
        self.tabview.tab("Settings").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Settings").grid_rowconfigure(0, weight=1)
        self.settingsDisplay = SettingsTab.SettingsTab(self.tabview.tab("Settings"))
        self.settingsDisplay.grid(row=0, column=0, sticky="nsew")
        

    ############################## FUNCTIONS ###############################
    # change frame to LoginPage
    def logout(self, controller):
        controller.show_frame("LoginPage", controller.id)

    # path of assets
    def asset_path(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)
