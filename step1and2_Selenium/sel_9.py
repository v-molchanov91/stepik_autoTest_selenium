from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(5)

    activ_button = browser.find_element(By.XPATH, "//button[@type='submit']")
    activ_button.click()
    browser.switch_to.alert.accept()
    x = int(browser.find_element(By.ID, "input_value").text)

    def calc(x):
        return math.log(abs(12*math.sin(x)))

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(str(calc(x)))
    browser.find_element(By.XPATH, "//button[@type='submit']").click()
finally:
    time.sleep(10)

    browser.quit()

