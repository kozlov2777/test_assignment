from selenium.webdriver.common.by import By


class InventoryPageLocator:
    """Locators for the inventory page elements."""

    LOGO_TITLE = (By.XPATH, '//*[@class="app_logo"]')

    CART_BUTTON = (By.XPATH, '//*[@id="shopping_cart_container"]')

    @staticmethod
    def item_price_text(index: int = 1) -> tuple[str, str]:
        """Get locator for the price text of an item by index.

        Args:
            index: The index of the item (starting from 1)

        Returns:
            Tuple containing By method and XPath locator
        """
        return (By.XPATH, f'(//div[@class="inventory_item"])[{index}]')

    @staticmethod
    def item_name_text(index: int = 1) -> tuple[str, str]:
        """Get locator for the name text of an item by index.

        Args:
            index: The index of the item (starting from 1)

        Returns:
            Tuple containing By method and XPath locator
        """
        return (By.XPATH, f'(//div[@class="inventory_item_name"])[{index}]')

    @staticmethod
    def item_description_text(index: int = 1) -> tuple[str, str]:
        """Get locator for the description text of an item by index.

        Args:
            index: The index of the item (starting from 1)

        Returns:
            Tuple containing By method and XPath locator
        """
        return (By.XPATH, f'(//div[@class="inventory_item_desc"])[{index}]')

    @staticmethod
    def add_to_card_button(index: int = 1) -> tuple[str, str]:
        """Get locator for the 'Add to Cart' button of an item by index.

        Args:
            index: The index of the item (starting from 1)

        Returns:
            Tuple containing By method and XPath locator
        """
        return (
            By.XPATH,
            f'(//button[@class="btn btn_primary btn_small btn_inventory "])[{index}]',
        )
