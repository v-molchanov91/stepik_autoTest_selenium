from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_FAILED = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators:
    ADD_TO_BASKET = (By.XPATH, "//button[@value='Add to basket']")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, ".alert-success .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
