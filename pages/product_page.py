from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.BASKET).click()

    def should_be_price_in_basket(self):
        assert self.is_element_present(*ProductPageLocators.PRICE), "Price is not presented"
        assert self.browser.find_element(*ProductPageLocators.PRICE).text == self.browser.find_element(*ProductPageLocators.PRICE_MASSAGE).text,  "Price not in basket, error"

    def should_be_name_book_in_basket(self):
        assert self.is_element_present(*ProductPageLocators.BOOK_NAME), "Book name is not presented"
        assert self.browser.find_element(*ProductPageLocators.BOOK_NAME).text == self.browser.find_element(*ProductPageLocators.BOOK_NAME_MASSAGE).text,  "Book name not in basket, error"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.BOOK_NAME_MASSAGE), \
        "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.BOOK_NAME_MASSAGE), \
        "Success message is not disappeared, but should be"