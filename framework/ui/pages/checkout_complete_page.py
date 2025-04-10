from framework.ui.locators.checkout_complete_page_locators import (
    CheckoutCompletePageLocators,
)
from framework.ui.pages.base_page import BasePage


class CheckoutCompletePage(BasePage):
    """Page object for the checkout completion page with order confirmation."""
    
    def get_title_text(self):
        """Get the title text of the checkout complete page.
        
        Returns:
            str: The title text (e.g., "Checkout: Complete!")
        """
        return self.get_text(locator=CheckoutCompletePageLocators.TITLE_TEXT)

    def get_complete_header_text(self):
        """Get the header text that confirms order completion.
        
        Returns:
            str: The header text (e.g., "Thank you for your order!")
        """
        return self.get_text(locator=CheckoutCompletePageLocators.COMPLETE_HEADER_TEXT)

    def get_complete_text(self):
        """Get the descriptive text about the order completion.
        
        Returns:
            str: The completion text with shipping information
        """
        return self.get_text(locator=CheckoutCompletePageLocators.COMPLETE_TEXT)
