from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try:
    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.XPATH, "//img")
    x = x_element.get_attribute("valuex")

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    y = calc(x)

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)
    chekbox = browser.find_element(By.ID, 'robotCheckbox')
    chekbox.click()
    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()
    button1 = browser.find_element(By.XPATH, "//button[@type='submit']")
    button1.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
