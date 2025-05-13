from .base_page import BasePage
from .locators import LoginPageLocators
from conftest import browser


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert current_url == "https://selenium1py.pythonanywhere.com/en-gb/accounts/login/", f"Expected login URL, but got {current_url}"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_elements_present(*LoginPageLocators.LOGIN_FORM), " is not login form"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_elements_present(*LoginPageLocators.REGISTER_FORM), "is not register form"
