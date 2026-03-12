from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class Shoppage():

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.shop_link = (By.CSS_SELECTOR, "a[href*='shop']")
        self.products = (By.XPATH, "//div[@class='card h-100']")
        self.addcart_btn = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def select_product(self, product_name):
        self.driver.find_element(*self.shop_link).click()
        products = self.driver.find_elements(*self.products)

        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == product_name:
                product.find_element(By.XPATH, "div/button").click()

    def cart(self):
        self.driver.find_element(*self.addcart_btn).click()