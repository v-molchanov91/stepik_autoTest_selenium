from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time


class TestRegistration(unittest.TestCase):
    def setUp(self):
            self.browser = webdriver.Chrome()

    def terdown(self):
        self.browser.quit()

    def fill_and_submit_form(self, link):
        self.browser.get(link)

        self.browser.find_element(By.XPATH, "//label[text()='First name*']/following-sibling::input").send_keys("Ivan")
        self.browser.find_element(By.XPATH, "//label[text()='Last name*']/following-sibling::input").send_keys("Petrov")
        self.browser.find_element(By.XPATH, "//label[text()='Email*']/following-sibling::input").send_keys("v.htr@mail.ru")

        self.browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        welcome_text_elt = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.TAG_NAME, "h1"))
        )
        return welcome_text_elt.text

    def test_registration_page1(self):
        welcome_text = self.fill_and_submit_form("https://suninjuly.github.io/registration1.html")
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

    def test_registration_page2(self):
        welcome_text = self.fill_and_submit_form("https://suninjuly.github.io/registration2.html")
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")


if __name__ == "__main__":
    unittest.main()
