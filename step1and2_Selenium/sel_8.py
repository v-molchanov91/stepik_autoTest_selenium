from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time


try:
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.XPATH, "//input[@name='firstname']")
    first_name.send_keys("Vladimir")
    last_name = browser.find_element(By.XPATH, "//input[@name='lastname']")
    last_name.send_keys("Molchanov")
    email = browser.find_element(By.XPATH, "//input[@name='email']")
    email.send_keys("V@mail.ru")
    upload_file = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    upload_file.send_keys(file_path)
    browser.find_element(By.XPATH, "//button[@type='submit']").click()

finally:
    time.sleep(10)

    browser.quit()
