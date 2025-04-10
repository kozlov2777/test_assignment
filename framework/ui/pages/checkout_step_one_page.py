from framework.ui.locators.checkout_step_one_page_locators import (
    CheckoutStepOnePageLocator,
)
from framework.ui.pages.base_page import BasePage


class CheckoutStepOnePage(BasePage):
    """Page object for the first step of checkout with customer information form."""

    def input_first_name_text(self, text: str):
        """Input first name in the checkout form.

        Args:
            text: First name to input
        """
        self.input_text(locator=CheckoutStepOnePageLocator.FIRSTNAME_INPUT, text=text)

    def input_last_name_text(self, text: str):
        """Input last name in the checkout form.

        Args:
            text: Last name to input
        """
        self.input_text(locator=CheckoutStepOnePageLocator.LASTNAME_INPUT, text=text)

    def input_postal_code_text(self, text: str):
        """Input postal code in the checkout form.

        Args:
            text: Postal code to input
        """
        self.input_text(locator=CheckoutStepOnePageLocator.POSTAL_CODE_INPUT, text=text)

    def click_continue_button(self):
        """Click the continue button to proceed to the next checkout step."""
        self.click_element(locator=CheckoutStepOnePageLocator.CONTINUE_BUTTON)
