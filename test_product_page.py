import time
import pytest

from .pages.locators import LoginPageLocators
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage
from .pages.main_page import MainPage


linkWithPromo = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'


@pytest.mark.user_add_basket
class TestGuestAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = 'qwerty123' + str(time.time())
        login_page = LoginPage(browser, LoginPageLocators.LOGIN_URL)
        login_page.open()
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
        page = MainPage(browser, link)
        product_page = ProductPage(browser, browser.current_url)
        page.open()
        product_page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
        page = MainPage(browser, link)
        page.open()
        product_page = ProductPage(browser, browser.current_url)
        product_page.add_to_basket()
        product_page.should_be_price_in_basket()
        product_page.should_be_name_book_in_basket()


def test_guest_should_see_login_link_on_product_page(browser):
    linkProductPage = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, linkProductPage)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    linkProductPage = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, linkProductPage)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
@pytest.mark.parametrize('parametrize_link',
                         ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                          pytest.param(
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                              marks=pytest.mark.xfail),
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, parametrize_link):
    page = MainPage(browser, parametrize_link)
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.add_to_basket()
    page.solve_quiz_and_get_code()
    product_page.should_be_price_in_basket()
    product_page.should_be_name_book_in_basket()


@pytest.mark.skip()
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = MainPage(browser, linkWithPromo)
    product_page = ProductPage(browser, browser.current_url)

    page.open()
    product_page.add_to_basket()
    page.solve_quiz_and_get_code()
    product_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = MainPage(browser, linkWithPromo)
    product_page = ProductPage(browser, browser.current_url)

    page.open()
    product_page.should_not_be_success_message()


@pytest.mark.skip()
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = MainPage(browser, linkWithPromo)
    product_page = ProductPage(browser, browser.current_url)

    page.open()
    product_page.add_to_basket()
    page.solve_quiz_and_get_code()
    product_page.should_disappeared_success_message()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    linkProductPage = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

    product_page = ProductPage(browser, linkProductPage)
    basket_page = BasketPage(browser, browser.current_url)

    product_page.open()
    product_page.should_be_basket_link()
    product_page.go_to_basket_page()

    basket_page.should_not_be_product_in_basket()
    basket_page.should_be_massage_empty_basket()
