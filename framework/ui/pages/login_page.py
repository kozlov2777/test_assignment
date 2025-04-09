from framework.ui.locators.login_page_locators import LoginPageLocators
from framework.ui.pages.base_page import BasePage


class LoginPage(BasePage):
    def get_text_login_title(self):
        return self.get_text(locator=LoginPageLocators.LOGO_TITLE)

    def input_username(self, username: str):
        self.input_text(locator=LoginPageLocators.USERNAME_INPUT, text=username)

    def get_placeholder_username(self):
        return self.get_attribute(
            locator=LoginPageLocators.USERNAME_INPUT, attribute="placeholder"
        )

    def input_password(self, password: str):
        self.input_text(locator=LoginPageLocators.PASSWORD_INPUT, text=password)

    def get_placeholder_password(self):
        return self.get_attribute(
            locator=LoginPageLocators.PASSWORD_INPUT, attribute="placeholder"
        )

    def click_login_button(self):
        self.click_element(locator=LoginPageLocators.LOGIN_BUTTON)

    def get_credentials(self):
        usernames = self.get_text(locator=LoginPageLocators.USERNAMES_TEXT)
        passwords = self.get_text(locator=LoginPageLocators.PASSWORD_TEXT)

        username = usernames.split("\n")[1]
        password = passwords.split("\n")[-1]
        return username, password
