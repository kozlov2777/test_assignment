from selenium.webdriver.common.by import By


class CheckoutCompletePageLocators:
    """Locators for the checkout complete page with order confirmation."""

    TITLE_TEXT = (By.XPATH, '//*[@class="title"]')
    COMPLETE_HEADER_TEXT = (By.XPATH, '//*[@class="complete-header"]')
    COMPLETE_TEXT = (By.XPATH, '//*[@class="complete-text"]')

    COMPLETE_IMAGE = (By.XPATH, '//*[@class="pony_express"]')
