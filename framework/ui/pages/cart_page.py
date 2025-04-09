from framework.ui.locators.cart_page_locators import CartPageLocators
from framework.ui.pages.base_page import BasePage


class CartPage(BasePage):
    def click_remove_button_by_index(self, index: int = 1):
        self.click_element(locator=CartPageLocators.remove_button(index=index))

    def get_item_price_text(self, index: int = 1) -> str:
        return self.get_text(locator=CartPageLocators.item_price_text(index=index))

    def click_checkout_button(self):
        self.click_element(locator=CartPageLocators.CHECKOUT_BUTTON)
