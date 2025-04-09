from selenium.webdriver.common.by import By


class CheckoutStepOnePageLocator:
    FIRSTNAME_INPUT = (By.XPATH, '//*[@id="first-name"]')
    LASTNAME_INPUT = (By.XPATH, '//*[@id="last-name"]')
    POSTAL_CODE_INPUT = (By.XPATH, '//*[@id="postal-code"]')

    CONTINUE_BUTTON = (By.XPATH, '//*[@id="continue"]')
