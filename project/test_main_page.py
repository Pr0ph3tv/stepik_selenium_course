import pytest

from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.parametrize('offer_number', [pytest.param(number, marks=pytest.mark.xfail(number == 7, reason=''))
                                          for number in range(10)])
def test_guest_can_add_product_to_basket(browser, offer_number):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer_number}"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_notification_that_product_is_added_to_basket()
    page.is_product_name_in_notification_equal_to_description()
    page.should_be_notification_with_total_basket_cost()
    page.is_product_price_equal_to_basket_cost()
