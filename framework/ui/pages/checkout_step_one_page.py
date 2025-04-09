from framework.ui.locators.checkout_step_one_page_locators import (
    CheckoutStepOnePageLocator,
)
from framework.ui.pages.base_page import BasePage


class CheckoutStepOnePage(BasePage):
    def input_first_name_text(self, text: str):
        self.input_text(locator=CheckoutStepOnePageLocator.FIRSTNAME_INPUT, text=text)

    def input_last_name_text(self, text: str):
        self.input_text(locator=CheckoutStepOnePageLocator.LASTNAME_INPUT, text=text)

    def input_postal_code_text(self, text: str):
        self.input_text(locator=CheckoutStepOnePageLocator.POSTAL_CODE_INPUT, text=text)

    def click_continue_button(self):
        self.click_element(locator=CheckoutStepOnePageLocator.CONTINUE_BUTTON)
