from customtkinter import CTkFrame, CTkLabel, CTkOptionMenu, StringVar, set_appearance_mode, set_widget_scaling
from utils import settings

class SettingsTab(CTkFrame):
    def __init__(self, parent, controller):
        self.controller = controller
        CTkFrame.__init__(self, parent)

        # settings tab grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(9, weight=1)

        # labels
        self.settingsLabel = CTkLabel(self, text="SETTINGS", font=("Arial", 15, "bold"))
        self.appearanceModeLabel = CTkLabel(self, text="Appearance Mode", anchor="w")
        self.colorThemeLabel = CTkLabel(self, text="Color Theme (requires restart)", anchor="w")
        self.tableThemeLabel = CTkLabel(self, text="Table Theme", anchor="w")
        self.scalingLabel = CTkLabel(self, text="UI Scaling", anchor="w")

        self.settingsLabel.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
        self.appearanceModeLabel.grid(row=1, column=1)
        self.colorThemeLabel.grid(row=3, column=1)
        self.tableThemeLabel.grid(row=5, column=1)
        self.scalingLabel.grid(row=7, column=1)

        # change  light or dark mode
        self.currentAppearance = StringVar(value=settings.appearance_read())
        self.appearanceModeOptionmenu = CTkOptionMenu(self, values=["Light", "Dark", "System"], command=self.change_appearance_mode_event, variable=self.currentAppearance)
        self.appearanceModeOptionmenu.grid(row=2, column=1, padx=20, pady=(2, 10))

        # change color theme
        self.currentTheme = StringVar(value=settings.theme_read())
        self.colorThemeOptionmenu = CTkOptionMenu(self, values=["blue", "dark-blue", "green"], command=self.set_default_color_theme_event, variable=self.currentTheme)
        self.colorThemeOptionmenu.grid(row=4, column=1, padx=20, pady=(2, 10))

        # change table theme
        self.currentTable = StringVar(value=settings.table_theme_read())
        self.tableThemeOptionmenu = CTkOptionMenu(self, values=["dark", "light"], command=self.set_default_table_theme_event, variable=self.currentTable)
        self.tableThemeOptionmenu.grid(row=6, column=1, padx=20, pady=(2, 10))

        # change scaling of ui
        self.currentScaling = StringVar(value=settings.scale_read())
        self.scalingOptionmenu = CTkOptionMenu(self, values=["80%", "90%", "100%", "110%", "120%"], command=self.change_scaling_event, variable=self.currentScaling)
        self.scalingOptionmenu.grid(row=8, column=1, padx=20, pady=(2, 10))

    ##### METHODS
    def change_appearance_mode_event(self, new_appearance_mode: str):
        # change appearance to light or dark
        set_appearance_mode(new_appearance_mode)
        settings.appearance_save(new_appearance_mode)

    def set_default_color_theme_event(self, new_default_color_theme: str):
        # change color theme (requires restart)
        settings.theme_save(new_default_color_theme)

    def set_default_table_theme_event(self, new_default_table_theme: str):
        # change table theme (requires restart)
        settings.table_theme_save(new_default_table_theme)
        self.controller.frames["InventoryPage"].accountDisplay.reload_treeview()
        self.controller.frames["InventoryPage"].dashboardDisplay.reload_treeview()
        self.controller.frames["InventoryPage"].inventoryDisplay.reload_treeview()

    def change_scaling_event(self, new_scaling: str):
        # change scaling of application
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        set_widget_scaling(new_scaling_float)
        settings.scale_save(new_scaling_float)

