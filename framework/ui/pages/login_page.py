from framework.ui.locators.login_page_locators import LoginPageLocators
from framework.ui.pages.base_page import BasePage


class LoginPage(BasePage):
    """Page object for the login page."""

    def get_text_login_title(self):
        """Get the text of the login page title."""
        return self.get_text(locator=LoginPageLocators.LOGO_TITLE)

    def input_username(self, username: str):
        """Input a username into the username field.

        Args:
            username: The username to input
        """
        self.input_text(locator=LoginPageLocators.USERNAME_INPUT, text=username)

    def get_placeholder_username(self):
        """Get the placeholder text for the username field."""
        return self.get_attribute(
            locator=LoginPageLocators.USERNAME_INPUT, attribute="placeholder"
        )

    def input_password(self, password: str):
        """Input a password into the password field.

        Args:
            password: The password to input
        """
        self.input_text(locator=LoginPageLocators.PASSWORD_INPUT, text=password)

    def get_placeholder_password(self):
        """Get the placeholder text for the password field."""
        return self.get_attribute(
            locator=LoginPageLocators.PASSWORD_INPUT, attribute="placeholder"
        )

    def click_login_button(self):
        """Click the login button to submit the login form."""
        self.click_element(locator=LoginPageLocators.LOGIN_BUTTON)

    def get_credentials(self):
        """Extract sample credentials from the login page.

        Returns:
            tuple: A tuple containing (username, password)
        """
        usernames = self.get_text(locator=LoginPageLocators.USERNAMES_TEXT)
        passwords = self.get_text(locator=LoginPageLocators.PASSWORD_TEXT)

        username = usernames.split("\n")[1]
        password = passwords.split("\n")[-1]
        return username, password
