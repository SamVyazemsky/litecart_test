from selenium import webdriver
from pages.product_page import ProductPage
from pages.main_page import MainPage
from pages.cart_page import CartPage


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.main_page = MainPage(self.driver)
        self.product_page = ProductPage(self.driver)

    def quit(self):
        self.driver.quit()

    def add_product_to_card(self):
        self.main_page.open()
        self.main_page.select_product()
        self.product_page(self.driver.current_url)
        self.product_page.set_size()
        q = self.product_page.check_quantity()
        self.product_page.add_to_cart()
        while self.product_page.check_quantity() == q:
            pass

    def remove_all_from_cart(self):
        self.cart_page.open()
        self.cart_page.del_from_cart()