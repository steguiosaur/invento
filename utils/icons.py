from customtkinter import CTkImage
from PIL import Image
from utils import Assets

class Icon():
    def __init__(self):

        self.search = CTkImage(
            light_image=Image.open(Assets.asset_path("./dark_search.png")),
            dark_image=Image.open(Assets.asset_path("./light_search.png")),
            size=(15, 15))

        self.categories = CTkImage(
            light_image=Image.open(Assets.asset_path("./dark_categories.png")),
            dark_image=Image.open(Assets.asset_path("./light_categories.png")),
            size=(64, 64))

        self.sales = CTkImage(
            light_image=Image.open(Assets.asset_path("./dark_coin_stack.png")),
            dark_image=Image.open(Assets.asset_path("./light_coin_stack.png")),
            size=(64, 64))

        self.products = CTkImage(
            light_image=Image.open(Assets.asset_path("./dark_package.png")),
            dark_image=Image.open(Assets.asset_path("./light_package.png")),
            size=(64, 64))

        self.user = CTkImage(
            light_image=Image.open(Assets.asset_path("./dark_user.png")),
            dark_image=Image.open(Assets.asset_path("./light_user.png")),
            size=(64, 64))

    def get_search(self):
        return self.search

    def get_categories(self):
        return self.categories

    def get_sales(self):
        return self.sales

    def get_products(self):
        return self.products

    def get_user(self):
        return self.user
