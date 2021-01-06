import pytest
from .pages.main_page import MainPage
from .pages.product_page import ProductPage
import time


@pytest.mark.parametrize('link', ["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6",
                                  pytest.param("offer7", marks=pytest.mark.xfail), "offer8", "offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    links = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={link}'
    page = ProductPage(browser, links)
    page.open()
    page.click_to_button()
    page.solve_quiz_and_get_code()
    page.should_be_basket()

