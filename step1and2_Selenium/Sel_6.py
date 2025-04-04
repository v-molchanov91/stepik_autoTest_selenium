from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = int(browser.find_element(By.ID, "num1").text)
    y = int(browser.find_element(By.ID, "num2").text)
    s = int(x) + int(y)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(str(s))
    button1 = browser.find_element(By.XPATH, "//button[@type='submit']")
    button1.click()

finally:
    time.sleep(10)
    browser.quit()
