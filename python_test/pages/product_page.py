from selenium.webdriver.support.wait import WebDriverWait


class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        # self.driver.get(url)
        return self

    def check_quantity(self):
        el = driver.find_element_by_css_selector('.quantity')
        return int(el.text)

    def set_size(self):
        size = driver.find_elements_by_css_selector('[name="options[Size]"]')
        if len(size) > 0:
            driver.find_element_by_css_selector('[name="options[Size]"]').click()
            driver.find_element_by_css_selector('select option[value="Small"]').click()

    def add_to_cart(self):
        driver.find_element_by_css_selector('button[type=submit][name="add_cart_product"]').click()
