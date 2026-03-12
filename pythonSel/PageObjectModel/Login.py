from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class Loginpage():

    def __init__(self,driver: WebDriver):
        self.driver = driver

        self.username = (By.ID, "username")
        self.password = (By.ID, "password")
        self.submitlogin = (By.XPATH, "//input[@type ='submit']")



    def login(self):
        self.driver.find_element(*self.username).send_keys("rahulshettyacademy")
        self.driver.find_element(*self.password).send_keys("Learning@830$3mK2")
        self.driver.find_element(*self.submitlogin).click()
