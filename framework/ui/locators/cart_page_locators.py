from selenium.webdriver.common.by import By


class CartPageLocators:
    CHECKOUT_BUTTON = (By.XPATH, '//*[@id="checkout"]')

    @staticmethod
    def remove_button(index: int = 1) -> tuple[str, str]:
        return (
            By.XPATH,
            f'(//button[@class="btn btn_secondary btn_small cart_button"])[{index}]',
        )

    @staticmethod
    def item_price_text(index: int = 1) -> tuple[str, str]:
        return (By.XPATH, f'(//div[@class="inventory_item_price"])[{index}]')
