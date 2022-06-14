import time

import pytest

from .pages.product_page import ProductPage
from .pages.main_page import MainPage

link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'


def test_guest_can_add_product_to_basket(browser):
    page = MainPage(browser, link)
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.add_to_basket()
    page.solve_quiz_and_get_code()
    product_page.should_be_price_in_basket()
    product_page.should_be_name_book_in_basket()

@pytest.mark.skip()
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = MainPage(browser, link)
    product_page = ProductPage(browser, browser.current_url)

    page.open()
    product_page.add_to_basket()
    page.solve_quiz_and_get_code()
    product_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = MainPage(browser, link)
    product_page = ProductPage(browser, browser.current_url)

    page.open()
    product_page.should_not_be_success_message()


@pytest.mark.skip()
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = MainPage(browser, link)
    product_page = ProductPage(browser, browser.current_url)

    page.open()
    product_page.add_to_basket()
    page.solve_quiz_and_get_code()
    product_page.should_disappeared_success_message()
