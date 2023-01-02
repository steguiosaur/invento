from customtkinter import CTkFrame, CTkButton

class InventoryPage(CTkFrame):
    def __init__(self, parent, controller):
        CTkFrame.__init__(self, parent)

        # create sidebar frame with widgets
        self.sidebar_frame = CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.sidebar_button_1 = CTkButton(self.sidebar_frame, command=lambda: self.go_login(controller))
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)

    def go_login(self, controller):
        controller.show_frame("LoginPage", controller.id)
