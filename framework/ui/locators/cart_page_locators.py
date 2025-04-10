from selenium.webdriver.common.by import By


class CartPageLocators:
    """Locators for the shopping cart page elements."""

    CHECKOUT_BUTTON = (By.XPATH, '//*[@id="checkout"]')

    @staticmethod
    def remove_button(index: int = 1) -> tuple[str, str]:
        """Get locator for the remove button of an item by index.

        Args:
            index: The index of the item (starting from 1)

        Returns:
            Tuple containing By method and XPath locator
        """
        return (
            By.XPATH,
            f'(//button[@class="btn btn_secondary btn_small cart_button"])[{index}]',
        )

    @staticmethod
    def item_price_text(index: int = 1) -> tuple[str, str]:
        """Get locator for the price text of an item in cart by index.

        Args:
            index: The index of the item (starting from 1)

        Returns:
            Tuple containing By method and XPath locator
        """
        return (By.XPATH, f'(//div[@class="inventory_item_price"])[{index}]')
