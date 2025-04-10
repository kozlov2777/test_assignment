from framework.ui.locators.cart_page_locators import CartPageLocators
from framework.ui.pages.base_page import BasePage


class CartPage(BasePage):
    """Page object for the shopping cart page."""

    def click_remove_button_by_index(self, index: int = 1):
        """Click the remove button for a specific product in the cart by index.

        Args:
            index: The index of the product in the cart (starting from 1)
        """
        self.click_element(locator=CartPageLocators.remove_button(index=index))

    def get_item_price_text(self, index: int = 1) -> str:
        """Get the price text of a product in the cart by index.

        Args:
            index: The index of the product in the cart (starting from 1)

        Returns:
            str: The price text of the product
        """
        return self.get_text(locator=CartPageLocators.item_price_text(index=index))

    def click_checkout_button(self):
        """Click the checkout button to proceed to checkout."""
        self.click_element(locator=CartPageLocators.CHECKOUT_BUTTON)
