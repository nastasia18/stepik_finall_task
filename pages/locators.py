from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    TITLE_BOOK = (By.CSS_SELECTOR, ".product_main h1")
    TITLE_BOOK_BASKET = (By.CSS_SELECTOR, ".alertinner strong")
    MESSAGE = (By.CSS_SELECTOR, "#messages .alert:first-child")
    PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRICE_BASKET = (By.CSS_SELECTOR, ".alertinner p strong")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

