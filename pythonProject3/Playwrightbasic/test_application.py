
import playwright.sync_api
from playwright.sync_api import expect


def test_application(playwright):
    button = playwright.chromium.launch(headless=False)
    page = button.new_page()
    page.goto ("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learniing@830$3mK2")
    page.get_by_role("combobox").select_option("consult")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password")).to_be_visible()
