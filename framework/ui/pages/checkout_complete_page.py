from framework.ui.locators.checkout_complete_page_locators import (
    CheckoutCompletePageLocators,
)
from framework.ui.pages.base_page import BasePage


class CheckoutCompletePage(BasePage):
    def get_title_text(self):
        return self.get_text(locator=CheckoutCompletePageLocators.TITLE_TEXT)

    def get_complete_header_text(self):
        return self.get_text(locator=CheckoutCompletePageLocators.COMPLETE_HEADER_TEXT)

    def get_complete_text(self):
        return self.get_text(locator=CheckoutCompletePageLocators.COMPLETE_TEXT)
