from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL)
        pass_input = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASS)
        pass_confirm_input = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASS_CONFIRM)
        button_register = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)

        email_input.send_keys(email)
        pass_input.send_keys(password)
        pass_confirm_input.send_keys(password)
        button_register.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "accounts/login/" in self.browser.current_url, "url error"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
