from selenium.webdriver.common.by import By


class CheckoutStepTwoPageLocator:
    ITEM_TOTAL_TEXT = (By.XPATH, '//*[@class="summary_subtotal_label"]')
    TAX_TEXT = (By.XPATH, '//*[@class="summary_tax_label"]')
    TOTAL_TEXT = (By.XPATH, '//*[@class="summary_total_label"]')

    FINISH_BUTTON = (By.XPATH, '//*[@id="finish"]')
