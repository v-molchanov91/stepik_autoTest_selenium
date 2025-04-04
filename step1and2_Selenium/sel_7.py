import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math


# browser = webdriver.Chrome()
# browser.execute_script("document.title='Script executing';alert('Robots at work');")
# time.sleep(10)


browser = webdriver.Chrome()
link = "https://suninjuly.github.io/execute_script.html"
browser.get(link)

try:
    x = int(browser.find_element(By.ID, "input_value").text)
    def calc(x):
        return str(math.log(abs(12*math.sin(x))))

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(calc(x))
    browser.find_element(By.ID, "robotCheckbox").click()
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    browser.find_element(By.ID, "robotsRule").click()
    button.click()
finally:
    time.sleep(10)

    browser.quit()

