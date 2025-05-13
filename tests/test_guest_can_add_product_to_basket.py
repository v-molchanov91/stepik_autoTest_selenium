from pages.main_page import MainPage
from pages.product_page import ProductPage


def test_added_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = MainPage(browser, link)
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.add_product_to_basket()

