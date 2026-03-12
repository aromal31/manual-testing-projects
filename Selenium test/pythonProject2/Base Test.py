from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Import login function
from login_page import login

# Launch browser
driver = webdriver.Chrome()

# Open site
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

# 🔥 Call login function
login(driver)

# Navigate to Leave module
driver.find_element(By.XPATH, "//span[text()='Leave']").click()
time.sleep(2)

driver.find_element(By.XPATH, "//a[text()='Leave List']").click()
time.sleep(2)

print("Leave page opened successfully")

# driver.quit()  # Optional