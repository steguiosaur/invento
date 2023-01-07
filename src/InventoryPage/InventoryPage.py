from customtkinter import CTkFrame, CTkButton, CTkLabel, CTkImage, CTkOptionMenu, CTkTabview, set_appearance_mode, set_widget_scaling, set_default_color_theme
from tkinter import ttk
from pathlib import Path
from PIL import Image

class InventoryPage(CTkFrame):

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("../assets")

    def __init__(self, parent, controller):
        CTkFrame.__init__(self, parent)

        self.refresh_unfocused()

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
        self.tabview.add("Inventory")
        self.tabview.add("Performance")
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

        self.inventoryButton = CTkButton(self.sidebarFrame, text="Inventory", command=lambda: self.tabview.set("Inventory"))
        self.inventoryButton.grid(row=4, column=0, padx=20, pady=10)

        self.accountMenuButton = CTkButton(self.sidebarFrame, text="Performance", command=lambda: self.tabview.set("Performance"))
        self.accountMenuButton.grid(row=5, column=0, padx=20, pady=10)

        self.accountMenuButton = CTkButton(self.sidebarFrame, text="Account", command=lambda: self.tabview.set("Account"))
        self.accountMenuButton.grid(row=6, column=0, padx=20, pady=10)

        self.settingsMenuButton = CTkButton(self.sidebarFrame, text="Settings", command=lambda: self.tabview.set("Settings"))
        self.settingsMenuButton.grid(row=7, column=0, padx=20, pady=10)

        self.aboutMenuButton = CTkButton(self.sidebarFrame, text="About", command=lambda: self.tabview.set("About"))
        self.aboutMenuButton.grid(row=8, column=0, padx=20, pady=10)

        self.logoutButton = CTkButton(self.sidebarFrame, text="Logout", command=lambda: self.logout(controller))
        self.logoutButton.grid(row=10, column=0, padx=20, pady=20)

        ############################ INVENTORY
        # inventory tab grid
        self.tabview.tab("Inventory").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Inventory").grid_columnconfigure(1, weight=1)
        self.tabview.tab("Inventory").grid_columnconfigure(2, weight=1)
        self.tabview.tab("Inventory").grid_columnconfigure(3, weight=1)
        self.tabview.tab("Inventory").grid_rowconfigure(0, weight=1)
        self.tabview.tab("Inventory").grid_rowconfigure(1, weight=1)
        self.tabview.tab("Inventory").grid_rowconfigure(2, weight=1)
        self.tabview.tab("Inventory").grid_rowconfigure(3, weight=0)

        # create frame for table
        self.tableFrame = CTkFrame(self.tabview.tab("Inventory"))
        self.tableFrame.grid(row=0, column=0, rowspan=3, columnspan=4, padx=(10, 10), pady=(10, 10), sticky="nsew")
        self.tableFrame.grid_columnconfigure(0, weight=1)
        self.tableFrame.rowconfigure(0, weight=1)

        self.treeViewStyle = ttk.Style()
        self.treeViewStyle.configure(
            "Treeview",
            background="#4b4b4b",
            foreground="white",
            rowheight="20",
            fieldbackground="#2b2b2b"
        )
        self.treeView = ttk.Treeview(self.tableFrame, selectmode='browse')
        self.treeView.grid(row=0, column=0, rowspan=1, columnspan=1,padx=(10,10), pady=(10,10), sticky="nsew")

        self.modifyItemFrame = CTkFrame(self.tabview.tab("Inventory"))
        self.modifyItemFrame.grid(row=3, column=0, rowspan=1, columnspan=2, padx=(10, 10), pady=(10, 10), sticky="nsew")

        self.updateItemFrame = CTkFrame(self.tabview.tab("Inventory"))
        self.updateItemFrame.grid(row=3, column=2, rowspan=1, columnspan=2, padx=(10, 10), pady=(10, 10), sticky="nsew")

        ############################# ACCOUNT

        ############################ ABOUTMENU
        
        ############################# SETTINGS
        # settings tab grid
        self.tabview.tab("Settings").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Settings").grid_columnconfigure(1, weight=0)
        self.tabview.tab("Settings").grid_columnconfigure(2, weight=1)
        self.tabview.tab("Settings").grid_rowconfigure(0, weight=0)

        # change to light or dark mode
        self.appearance_mode_label = CTkLabel(self.tabview.tab("Settings"), text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=1, column=1, padx=20, pady=(10, 0))

        self.appearance_mode_optionemenu = CTkOptionMenu(self.tabview.tab("Settings"), values=["Light", "Dark", "System"], command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=2, column=1, padx=20, pady=(10, 10))

        # change color theme
        self.color_theme_label = CTkLabel(self.tabview.tab("Settings"), text="Color Theme:", anchor="w")
        self.color_theme_label.grid(row=3, column=1, padx=20, pady=(10, 0))

        self.color_theme_optionmenu = CTkOptionMenu(self.tabview.tab("Settings"), values=["blue", "dark-blue", "green"], command=self.set_default_color_theme_event)
        self.color_theme_optionmenu.grid(row=4, column=1, padx=20, pady=(10, 10))

        # change scaling of ui
        self.scaling_label = CTkLabel(self.tabview.tab("Settings"), text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=5, column=1, padx=20, pady=(10, 0))

        self.scaling_optionemenu = CTkOptionMenu(self.tabview.tab("Settings"), values=["80%", "90%", "100%", "110%", "120%"], command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=6, column=1, padx=20, pady=(10, 20))

    ############################## FUNCTIONS ###############################
    def logout(self, controller):
        controller.show_frame("LoginPage", controller.id)

    def change_appearance_mode_event(self, new_appearance_mode: str):
        set_appearance_mode(new_appearance_mode)

    def set_default_color_theme_event(self, new_default_color_theme: str):
        set_default_color_theme(new_default_color_theme)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        set_widget_scaling(new_scaling_float)

    # refresh placeholder_text and password show to *
    def refresh_unfocused(self):
        self.focus_set()

    # path of assets
    def asset_path(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)
