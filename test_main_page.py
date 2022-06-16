import pytest
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.main_page import MainPage


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        main_page = MainPage(browser, link)
        basket_page = BasketPage(browser, link)

        main_page.open()
        main_page.should_be_basket_link()
        main_page.go_to_basket_page()

        basket_page.should_not_be_product_in_basket()
        basket_page.should_be_massage_empty_basket()
