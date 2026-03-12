from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Checkoutthepage:

    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.XPATH, "//button[@class='btn btn-success']")
        self.country_input = (By.ID, "country")
        self.country_option = (By.LINK_TEXT, "India")
        self.checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
        self.purchase_button = (By.CSS_SELECTOR, "[type='submit']")
        self.success_message = (By.CLASS_NAME, "alert-success")

    def checkout(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.checkout_button)).click()

    def useraddress(self, country):
        self.driver.find_element(*self.country_input).send_keys(country)

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.country_option)).click()

        self.driver.find_element(*self.checkbox).click()
        self.driver.find_element(*self.purchase_button).click()

    def validation(self):
        successText = self.driver.find_element(*self.success_message).text
        assert "Success! Thank you!" in successText