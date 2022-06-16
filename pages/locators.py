from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a[href*='/basket/']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_URL = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_FORM_EMAIL = (By.CSS_SELECTOR, "#register_form input[name='registration-email']")
    REGISTER_FORM_PASS = (By.CSS_SELECTOR, "#register_form input[name='registration-password1']")
    REGISTER_FORM_PASS_CONFIRM = (By.CSS_SELECTOR, "#register_form input[name='registration-password2']")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form button[name='registration_submit']")


class ProductPageLocators():
    BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRICE = (By.CSS_SELECTOR, 'p.price_color')
    PRICE_MASSAGE = (By.CSS_SELECTOR, '.alertinner p strong')
    BOOK_NAME = (By.CSS_SELECTOR, '.product_main h1')
    BOOK_NAME_MASSAGE = (By.CSS_SELECTOR, '.alertinner strong')


class BasketPageLocators():
    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, '#content_inner p')
    PRODUCT_BLOCK = (By.CSS_SELECTOR, '.basket-items')
