from selenium.webdriver.common.by import By


class LoginPageLocators:
    """Locators for the login page elements."""

    LOGO_TITLE = (By.XPATH, '//div[@class="login_logo"]')

    USERNAME_INPUT = (By.XPATH, '//*[@id="user-name"]')
    PASSWORD_INPUT = (By.XPATH, '//*[@id="password"]')

    LOGIN_BUTTON = (By.XPATH, '//*[@id="login-button"]')

    USERNAMES_TEXT = (By.XPATH, '//*[@id="login_credentials"]')
    PASSWORD_TEXT = (By.XPATH, '//*[@class="login_password"]')
