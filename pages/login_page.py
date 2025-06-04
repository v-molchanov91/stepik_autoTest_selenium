from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert "login" in current_url, f"Expected login URL, but got {current_url}"

    def should_be_login_form(self):
        assert self.is_elements_present(*LoginPageLocators.LOGIN_FORM), " is not login form"

    def should_be_register_form(self):
        assert self.is_elements_present(*LoginPageLocators.REGISTER_FORM), "is not register form"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        password_input = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        confirm_password_input = self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)

        email_input.send_keys(email)
        password_input.send_keys(password)
        confirm_password_input.send_keys(password)
        register_button.click()

