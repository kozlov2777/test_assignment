import pytest
import allure
from typing import Tuple

from framework.ui.pages.login_page import LoginPage
from framework.ui.pages.inventory_page import InventoryPage


@pytest.fixture
def logged_in_user(driver) -> Tuple[InventoryPage, str]:
    """
    Fixture for user login process

    Returns:
        Tuple[InventoryPage, str]: Inventory page instance and username
    """
    with allure.step("Initialize login page"):
        login_page = LoginPage(driver=driver, url="https://www.saucedemo.com/")
        login_page.open()

    with allure.step("Get credentials"):
        username, password = login_page.get_credentials()
        allure.attach(
            username, name="Username", attachment_type=allure.attachment_type.TEXT
        )

    with allure.step("Login with credentials"):
        login_page.input_username(username=username)
        login_page.input_password(password=password)
        login_page.click_login_button()

    with allure.step("Verify successful login"):
        current_url = login_page.get_current_url()
        allure.attach(
            current_url,
            name="Redirect URL",
            attachment_type=allure.attachment_type.TEXT,
        )
        assert (
            current_url == "https://www.saucedemo.com/inventory.html"
        ), f"Login failed. URL: {current_url}"

    with allure.step("Initialize inventory page"):
        inventory_page = InventoryPage(driver=driver)

    return inventory_page, username
