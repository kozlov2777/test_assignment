import pytest
import allure

from framework.ui.pages.cart_page import CartPage
from framework.ui.pages.checkout_complete_page import CheckoutCompletePage
from framework.ui.pages.checkout_step_one_page import CheckoutStepOnePage
from framework.ui.pages.checkout_step_two_page import CheckoutStepTwoPage
from framework.ui.pages.inventory_page import InventoryPage
from framework.ui.pages.login_page import LoginPage


@pytest.fixture
def login_page(driver) -> LoginPage:
    with allure.step("Initialize login page"):
        page = LoginPage(driver=driver, url="https://www.saucedemo.com/")
        page.open()
    return page


@pytest.fixture
def inventory_page(driver) -> InventoryPage:
    with allure.step("Initialize inventory page"):
        page = InventoryPage(driver=driver)
    return page


@pytest.fixture
def cart_page(driver) -> CartPage:
    with allure.step("Initialize cart page"):
        page = CartPage(driver=driver)
    return page


@pytest.fixture
def checkout_step_one_page(driver) -> CheckoutStepOnePage:
    with allure.step("Initialize checkout step one page"):
        page = CheckoutStepOnePage(driver=driver)
    return page


@pytest.fixture
def checkout_step_two_page(driver) -> CheckoutStepTwoPage:
    with allure.step("Initialize checkout step two page"):
        page = CheckoutStepTwoPage(driver=driver)
    return page


@pytest.fixture
def checkout_complete_page(driver) -> CheckoutCompletePage:
    with allure.step("Initialize checkout complete page"):
        page = CheckoutCompletePage(driver=driver)
    return page


@pytest.fixture
def get_credentials(login_page):
    with allure.step("Get user credentials"):
        credentials = login_page.get_credentials()
        allure.attach(
            credentials[0], name="Username", attachment_type=allure.attachment_type.TEXT
        )
    return credentials
