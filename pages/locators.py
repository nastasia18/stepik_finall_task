from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_AGAIN = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_REG = (By.CSS_SELECTOR, '[name="registration_submit"]')


class ProductPageLocators:
    BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    TITLE_BOOK = (By.CSS_SELECTOR, ".product_main h1")
    TITLE_BOOK_BASKET = (By.CSS_SELECTOR, ".alertinner strong")
    MESSAGE = (By.CSS_SELECTOR, "#messages .alert:first-child")
    PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRICE_BASKET = (By.CSS_SELECTOR, ".alertinner p strong")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BUTTON_BASKET = (By.CSS_SELECTOR, ".btn-group")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "#content_inner h2")
    TEXT_EMPTY = (By.CSS_SELECTOR, "#content_inner p")
