from selenium.webdriver.support.wait import WebDriverWait


class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("http://localhost/litecart/en")
        return self

    def check_quantity(self):
        el = self.driver.find_element_by_css_selector('.quantity')
        return int(el.text)

    def select_product(self):
        el = self.driver.find_element_by_css_selector('.product.column.shadow.hover-light')
        el.click()
