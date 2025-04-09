from framework.ui.locators.cheackout_step_two_page_locators import (
    CheckoutStepTwoPageLocator,
)
from framework.ui.pages.base_page import BasePage


class CheckoutStepTwoPage(BasePage):
    def get_item_total_text(self) -> str:
        return self.get_text(locator=CheckoutStepTwoPageLocator.ITEM_TOTAL_TEXT)

    def get_tax_text(self) -> str:
        return self.get_text(locator=CheckoutStepTwoPageLocator.TAX_TEXT)

    def get_total_text(self) -> str:
        return self.get_text(locator=CheckoutStepTwoPageLocator.TOTAL_TEXT)

    def click_finish_button(self):
        self.click_element(locator=CheckoutStepTwoPageLocator.FINISH_BUTTON)
