from .base_page import BasePage
from .locators import ProductPageLocators


#  Нажимаем кнопку Добавить в корзину
class ProductPage(BasePage):
    def click_to_button(self):
        self.should_be_button()
        btn = self.browser.find_element(*ProductPageLocators.BUTTON)
        btn.click()

    def should_be_button(self):
        # проверка, что есть кнопка Добавить в корзину
        assert self.is_element_present(*ProductPageLocators.BUTTON), "Button 'add to basket' is not presented"

    def should_be_basket(self):
        # проверка корзины
        self.should_be_product_name()
        self.should_be_price()
        self.should_be_success_message()

    def should_be_product_name(self):
        # проверка, что название книги соответствующее
        title_book = self.browser.find_element(*ProductPageLocators.TITLE_BOOK)
        title_book_basket = self.browser.find_element(*ProductPageLocators.TITLE_BOOK_BASKET)
        assert title_book.text == title_book_basket.text, "Title book does not match"

    def should_be_price(self):
        # проверка, что цены соответствующее
        price = self.browser.find_element(*ProductPageLocators.PRICE)
        price_basket = self.browser.find_element(*ProductPageLocators.PRICE_BASKET)
        assert price.text == price_basket.text, "Price does not match"

    def should_be_success_message(self):
        # проверка, что есть сообщение о том, что товар добавлен в корзину
        message = self.browser.find_element(*ProductPageLocators.MESSAGE)
        title_book_basket = self.browser.find_element(*ProductPageLocators.TITLE_BOOK_BASKET)
        assert title_book_basket.text in message.text, "Message is not presented"

    def should_not_be_success_message(self):
        # проверка, что нет сообщения о том, что товар добавлен в корзину
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE), \
            "Success message is presented, but should not be"

    def should_is_disappeared_success_message(self):
        # проверка, что сообщение исчезает через какое-то время
        assert self.is_disappeared(*ProductPageLocators.MESSAGE), \
            "Success message is not disappeared, but should not be"
