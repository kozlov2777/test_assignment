from framework.ui.locators.inventory_page_locators import InventoryPageLocator
from framework.ui.pages.base_page import BasePage


class InventoryPage(BasePage):
    """Page object for the inventory/products page."""

    def clict_add_to_card_item(self, index: int = 1):
        """Click the 'Add to Cart' button for a specific product by index.

        Args:
            index: The index of the product (starting from 1)
        """
        self.click_element(locator=InventoryPageLocator.add_to_card_button(index=index))

    def get_item_price_text(self, index: int = 1):
        """Get the price text of a product by index.

        Args:
            index: The index of the product (starting from 1)

        Returns:
            str: The price text of the product
        """
        return self.get_text(locator=InventoryPageLocator.item_price_text(index=index))

    def get_item_description(self, index: int = 1):
        """Get the description text of a product by index.

        Args:
            index: The index of the product (starting from 1)

        Returns:
            str: The description text of the product
        """
        return self.get_text(
            locator=InventoryPageLocator.item_description_text(index=index)
        )

    def click_cart_button(self):
        """Click the cart icon button to navigate to the cart page."""
        self.click_element(locator=InventoryPageLocator.CART_BUTTON)
