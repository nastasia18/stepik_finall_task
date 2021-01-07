from .base_page import BasePage
from .locators import BasketPageLocators, BasePageLocators


class BasketPage(BasePage):
    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), "Basket is not empty"

    def should_text_not_be_product_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_EMPTY), "Not text 'Basket is empty'"
