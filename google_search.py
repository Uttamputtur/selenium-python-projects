from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.google.com")

time.sleep(2)

search = driver.find_element(By.NAME, "q")

search.send_keys("Selenium Python")

time.sleep(5)

driver.quit()