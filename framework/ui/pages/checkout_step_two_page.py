from framework.ui.locators.cheackout_step_two_page_locators import (
    CheckoutStepTwoPageLocator,
)
from framework.ui.pages.base_page import BasePage


class CheckoutStepTwoPage(BasePage):
    """Page object for the second step of checkout with order summary."""
    
    def get_item_total_text(self) -> str:
        """Get the subtotal text for all items in the order.
        
        Returns:
            str: The subtotal text (e.g., "Item total: $29.99")
        """
        return self.get_text(locator=CheckoutStepTwoPageLocator.ITEM_TOTAL_TEXT)

    def get_tax_text(self) -> str:
        """Get the tax amount text for the order.
        
        Returns:
            str: The tax text (e.g., "Tax: $2.40")
        """
        return self.get_text(locator=CheckoutStepTwoPageLocator.TAX_TEXT)

    def get_total_text(self) -> str:
        """Get the total amount text for the order.
        
        Returns:
            str: The total text (e.g., "Total: $32.39")
        """
        return self.get_text(locator=CheckoutStepTwoPageLocator.TOTAL_TEXT)

    def click_finish_button(self):
        """Click the finish button to complete the order."""
        self.click_element(locator=CheckoutStepTwoPageLocator.FINISH_BUTTON)
