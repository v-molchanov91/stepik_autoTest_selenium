from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_shopping_cart(browser):
    browser.get(link)
    wait = WebDriverWait(browser, 10)
    add_to_cart_btn = wait.until(EC.visibility_of_element_located((By.XPATH, "//form[@id='add_to_basket_form'] /button")))
    assert add_to_cart_btn.is_displayed(), "Кнопка 'Добавить в корзину' не отображается на странице"

