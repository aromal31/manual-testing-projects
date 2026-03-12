from selenium.webdriver.remote.webdriver import WebDriver

from PageObjectModel.Login import Loginpage
from PageObjectModel.Shoppage import Shoppage
from PageObjectModel.checkoutpage import Checkoutthepage


def test_e2e(browserInstance):

    driver: WebDriver = browserInstance

    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    driver.maximize_window()

    loginpage = Loginpage(driver)
    loginpage.login()

    shoppage = Shoppage(driver)
    shoppage.select_product("Blackberry")
    shoppage.cart()

    checkout = Checkoutthepage(driver)
    checkout.checkout()
    checkout.useraddress("ind")
    checkout.validation()