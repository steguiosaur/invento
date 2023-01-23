from customtkinter import CTkFrame, CTkLabel, CTkOptionMenu, StringVar, set_appearance_mode, set_default_color_theme, set_widget_scaling
from Functionality import settings

class SettingsTab(CTkFrame):
    def __init__(self, parent):
        CTkFrame.__init__(self, parent)

        # settings tab grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=0)

        # change to light or dark mode
        self.appearanceModeLabel = CTkLabel(self, text="Appearance Mode:", anchor="w")
        self.appearanceModeLabel.grid(row=1, column=1, padx=20, pady=(10, 0))

        self.currentAppearance = StringVar(value=settings.appearance_read())

        self.appearanceModeOptionmenu = CTkOptionMenu(self, values=["Light", "Dark", "System"], command=self.change_appearance_mode_event, variable=self.currentAppearance)
        self.appearanceModeOptionmenu.grid(row=2, column=1, padx=20, pady=(10, 10))

        # change color theme
        self.colorThemeLabel = CTkLabel(self, text="Color Theme (requires restart):", anchor="w")
        self.colorThemeLabel.grid(row=3, column=1, padx=20, pady=(10, 0))

        self.currentTheme = StringVar(value=settings.theme_read())

        self.colorThemeOptionmenu = CTkOptionMenu(self, values=["blue", "dark-blue", "green"], command=self.set_default_color_theme_event, variable=self.currentTheme)
        self.colorThemeOptionmenu.grid(row=4, column=1, padx=20, pady=(10, 10))

        # change table theme
        self.tableThemeLabel = CTkLabel(self, text="Table Theme (requires restart):", anchor="w")
        self.tableThemeLabel.grid(row=5, column=1, padx=20, pady=(10, 0))

        self.currentTable = StringVar(value=settings.table_theme_read())

        self.tableThemeOptionmenu = CTkOptionMenu(self, values=["dark", "light"], command=self.set_default_table_theme_event, variable=self.currentTable)
        self.tableThemeOptionmenu.grid(row=6, column=1, padx=20, pady=(10, 10))

        # change scaling of ui
        self.scalingLabel = CTkLabel(self, text="UI Scaling:", anchor="w")
        self.scalingLabel.grid(row=7, column=1, padx=20, pady=(10, 0))

        self.currentScaling = StringVar(value=settings.scale_read())

        self.scalingOptionmenu = CTkOptionMenu(self, values=["80%", "90%", "100%", "110%", "120%"], command=self.change_scaling_event, variable=self.currentScaling)
        self.scalingOptionmenu.grid(row=8, column=1, padx=20, pady=(10, 20))

    # change appearance to light or dark
    def change_appearance_mode_event(self, new_appearance_mode: str):
        set_appearance_mode(new_appearance_mode)
        settings.appearance_save(new_appearance_mode)

    # change color theme (requires restart)
    def set_default_color_theme_event(self, new_default_color_theme: str):
        settings.theme_save(new_default_color_theme)

    # change table theme (requires restart)
    def set_default_table_theme_event(self, new_default_table_theme: str):
        settings.table_theme_save(new_default_table_theme)

    # change scaling of application
    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        set_widget_scaling(new_scaling_float)
        settings.scale_save(new_scaling_float)

