from selenium.webdriver.common.by import By


class InventoryPageLocator:
    LOGO_TITLE = (By.XPATH, '//*[@class="app_logo"]')

    CART_BUTTON = (By.XPATH, '//*[@id="shopping_cart_container"]')

    @staticmethod
    def item_price_text(index: int = 1) -> tuple[str, str]:
        return (By.XPATH, f'(//div[@class="inventory_item"])[{index}]')

    @staticmethod
    def item_name_text(index: int = 1) -> tuple[str, str]:
        return (By.XPATH, f'(//div[@class="inventory_item_name"])[{index}]')

    @staticmethod
    def item_description_text(index: int = 1) -> tuple[str, str]:
        return (By.XPATH, f'(//div[@class="inventory_item_desc"])[{index}]')

    @staticmethod
    def add_to_card_button(index: int = 1) -> tuple[str, str]:
        return (
            By.XPATH,
            f'(//button[@class="btn btn_primary btn_small btn_inventory "])[{index}]',
        )
