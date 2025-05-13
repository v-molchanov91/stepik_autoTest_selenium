from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.product_url()
        self.product_added_to_cart()
        self.basket_price()

    def product_url(self):
        current_url = self.browser.current_url
        assert "promo=newYear" in current_url, f"Expected promo in URL, got: {current_url}"

    def product_added_to_cart(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_button.click()
        self.solve_quiz_and_get_code()
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        success_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE).text
        assert product_name == success_message, f"Expected product name '{product_name}' in success message, but got '{success_message}'"

    def basket_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert product_price == basket_total, f"Expected basket total '{product_price}', but got '{basket_total}'"

