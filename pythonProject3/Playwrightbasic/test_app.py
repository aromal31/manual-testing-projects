import page
from playwright.sync_api import Page


def test_app(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("consult")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    iphone = page.locator("app-card").filter(has_text="iphone X")
    iphone.get_by_role("button").click()
    Nokia = page.locator("app-card").filter(has_text="Nokia Edge")
    Nokia.get_by_role("button").click()
    page.get_by_text("Checkout").click()