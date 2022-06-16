from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_massage_empty_basket(self):
        assert self.is_element_present(
            *BasketPageLocators.MESSAGE_EMPTY_BASKET), "Don't show massage about empty basket"

    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_BLOCK), "product is presented, but should not be"
