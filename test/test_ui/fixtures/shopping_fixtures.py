import pytest
import allure
from typing import Tuple
from decimal import Decimal

from framework.ui.pages.cart_page import CartPage
from framework.utils import extract_price_as_decimal


@pytest.fixture
def product_in_cart(driver, logged_in_user) -> Tuple[CartPage, Decimal]:
    """
    Fixture for adding products to cart and preparing for checkout

    Args:
        driver: WebDriver instance
        logged_in_user: Fixture for logged in user

    Returns:
        Tuple[CartPage, Decimal]: Cart page instance and product price
    """
    with allure.step("Prepare inventory page with logged in user"):
        inventory_page, _ = logged_in_user

    items_count = 3
    with allure.step(f"Add {items_count} products to cart"):
        for i in range(1, items_count + 1):
            with allure.step(f"Add product #{i} to cart"):
                inventory_page.clict_add_to_card_item(i)

    with allure.step("Open cart page"):
        inventory_page.click_cart_button()
        cart_page = CartPage(driver=driver)

    with allure.step("Remove all products except the first one"):
        for i in range(items_count, 1, -1):
            with allure.step(f"Remove product #{i} from cart"):
                cart_page.click_remove_button_by_index(i)

    with allure.step("Get price of the remaining product"):
        price_text = cart_page.get_item_price_text(1)
        price_decimal = extract_price_as_decimal(price_text)
        allure.attach(
            f"Product price: {price_text}",
            name="Product Price",
            attachment_type=allure.attachment_type.TEXT,
        )

    return cart_page, price_decimal
