from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "http://suninjuly.github.io/redirect_accept.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(5)

    browser.find_element(By.XPATH, "//button[@type='submit']").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    time.sleep(2)
    x = int(browser.find_element(By.ID, "input_value").text)

    def calc(x):
        return math.log(abs(12*math.sin(x)))
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(str(calc(x)))
    browser.find_element(By.XPATH, "//button[@type='submit']").click()
finally:
    time.sleep(10)

    browser.quit()
