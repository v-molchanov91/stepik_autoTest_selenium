from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.base_page import BasePage
import pytest
import time


@pytest.mark.login
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_link = "https://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, login_link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = "StrongPass123!"
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_cant_see_success_message(self, browser):
        link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()


@pytest.mark.need_review
@pytest.mark.skip()
@pytest.mark.parametrize('link', ["https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param(
                                   "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                   marks=pytest.mark.xfail(reason="Known bug on offer7")
                                  ),
                                  "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_added_product_to_basket(browser, link):
    page = MainPage(browser, link)
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.add_product_to_basket()


@pytest.mark.xfail(reason="update test")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link, 0)
    page.open()
    page.product_added_to_cart()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link, 0)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="update logic webpage")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link, 0)
    page.open()
    page.product_added_to_cart()
    page.not_be_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.no_items_in_the_cart()
    basket_page.text_in_the_basket()
