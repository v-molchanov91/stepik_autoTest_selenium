import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "https://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    button1 = browser.find_element(By.ID, "book")
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button1.click()
    x = int(browser.find_element(By.ID, "input_value").text)


    def calc(x):
        return math.log(abs(12 * math.sin(x)))


    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(str(calc(x)))
    browser.find_element(By.XPATH, "//button[@type='submit']").click()
finally:
    time.sleep(10)

    browser.quit()

