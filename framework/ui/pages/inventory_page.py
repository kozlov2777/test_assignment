from framework.ui.locators.inventory_page_locators import InventoryPageLocator
from framework.ui.pages.base_page import BasePage


class InventoryPage(BasePage):
    def clict_add_to_card_item(self, index: int = 1):
        self.click_element(locator=InventoryPageLocator.add_to_card_button(index=index))

    def get_item_price_text(self, index: int = 1):
        return self.get_text(locator=InventoryPageLocator.item_price_text(index=index))

    def get_item_description(self, index: int = 1):
        return self.get_text(
            locator=InventoryPageLocator.item_description_text(index=index)
        )

    def click_cart_button(self):
        self.click_element(locator=InventoryPageLocator.CART_BUTTON)
