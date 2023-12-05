from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд
try:

    browser.get("http://suninjuly.github.io/cats.html")
    button = browser.find_element(By.ID, "button")
finally:
    time.sleep(10)
    browser.quit()