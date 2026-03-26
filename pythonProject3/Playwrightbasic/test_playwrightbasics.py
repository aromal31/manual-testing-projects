import time

from playwright.sync_api import Page


def test_playwright(page:Page):
   page.goto("https://rahulshettyacademy.com/loginpagePractise/")
   page.get_by_label("Username:").fill("rahulshettyacademy")
   page.get_by_label("Password:").fill("Learning@830$3mK2")
   page.get_by_role("combobox").select_option("consult")
   page.locator("#terms").check()
   page.get_by_role("button", name="Sign In").click()


