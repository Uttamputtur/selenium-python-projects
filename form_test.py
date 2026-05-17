from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.NAME, "name").send_keys("Uttam")

driver.find_element(By.NAME, "email").send_keys("uttam@gmail.com")

driver.find_element(By.ID, "exampleCheck1").click()

dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))

dropdown.select_by_visible_text("Male")

driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

time.sleep(5)

driver.quit()