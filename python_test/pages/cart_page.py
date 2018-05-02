from selenium.webdriver.support.wait import WebDriverWait


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("http://localhost/litecart/en/checkout")
        return self

    def del_from_cart(self):
        while len(driver.find_elements_by_css_selector('li.shortcut')) > 0 or len(
                driver.find_elements_by_css_selector('button[name="remove_cart_item"]')) > 0:
            a = driver.find_element_by_css_selector('#box-checkout-summary')
            if len(driver.find_elements_by_css_selector('li.shortcut')) > 0:
                WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'li.shortcut'))).click()
                WebDriverWait(driver, 15).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[name="remove_cart_item"]'))).click()
                a = EC.visibility_of(driver.find_element_by_css_selector('#box-checkout-summary'))
            elif len(driver.find_elements_by_css_selector('button[name="remove_cart_item"]')) > 0:
                WebDriverWait(driver, 15).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[name="remove_cart_item"]'))).click()
                EC.staleness_of(a)