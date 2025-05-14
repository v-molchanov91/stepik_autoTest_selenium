from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def no_items_in_the_cart(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_CART), \
            "Basket has items, but should be empty"

    def text_in_the_basket(self):
        assert not self.is_not_element_present(*BasketPageLocators.SHOPPING_EMPTY_CART_TEXT), \
            "No message that basket is empty"
