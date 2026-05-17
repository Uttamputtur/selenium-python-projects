from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://rahulshettyacademy.com/loginpagePractise/")

driver.find_element(By.ID, "username").send_keys("rahulshettyacademy")

driver.find_element(By.ID, "password").send_keys("learning")

driver.find_element(By.ID, "signInBtn").click()

time.sleep(5)

driver.quit()