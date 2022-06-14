from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_URL = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")


class ProductPageLocators():
    BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRICE = (By.CSS_SELECTOR, 'p.price_color')
    PRICE_MASSAGE = (By.CSS_SELECTOR, '.alertinner p strong')
    BOOK_NAME = (By.CSS_SELECTOR, '.product_main h1')
    BOOK_NAME_MASSAGE = (By.CSS_SELECTOR, '.alertinner strong')
