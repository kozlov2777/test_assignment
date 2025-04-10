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
    """
    Fixture that provides a LoginPage instance.

    Args:
        driver: WebDriver instance from driver fixture

    Returns:
        LoginPage: Initialized login page with opened URL
    """
    with allure.step("Initialize login page"):
        page = LoginPage(driver=driver, url="https://www.saucedemo.com/")
        page.open()
    return page


@pytest.fixture
def inventory_page(driver) -> InventoryPage:
    """
    Fixture that provides an InventoryPage instance.

    Args:
        driver: WebDriver instance from driver fixture

    Returns:
        InventoryPage: Initialized inventory page
    """
    with allure.step("Initialize inventory page"):
        page = InventoryPage(driver=driver)
    return page


@pytest.fixture
def cart_page(driver) -> CartPage:
    """
    Fixture that provides a CartPage instance.

    Args:
        driver: WebDriver instance from driver fixture

    Returns:
        CartPage: Initialized cart page
    """
    with allure.step("Initialize cart page"):
        page = CartPage(driver=driver)
    return page


@pytest.fixture
def checkout_step_one_page(driver) -> CheckoutStepOnePage:
    """
    Fixture that provides a CheckoutStepOnePage instance.

    Args:
        driver: WebDriver instance from driver fixture

    Returns:
        CheckoutStepOnePage: Initialized checkout step one page
    """
    with allure.step("Initialize checkout step one page"):
        page = CheckoutStepOnePage(driver=driver)
    return page


@pytest.fixture
def checkout_step_two_page(driver) -> CheckoutStepTwoPage:
    """
    Fixture that provides a CheckoutStepTwoPage instance.

    Args:
        driver: WebDriver instance from driver fixture

    Returns:
        CheckoutStepTwoPage: Initialized checkout step two page
    """
    with allure.step("Initialize checkout step two page"):
        page = CheckoutStepTwoPage(driver=driver)
    return page


@pytest.fixture
def checkout_complete_page(driver) -> CheckoutCompletePage:
    """
    Fixture that provides a CheckoutCompletePage instance.

    Args:
        driver: WebDriver instance from driver fixture

    Returns:
        CheckoutCompletePage: Initialized checkout complete page
    """
    with allure.step("Initialize checkout complete page"):
        page = CheckoutCompletePage(driver=driver)
    return page


@pytest.fixture
def get_credentials(login_page):
    """
    Fixture that retrieves test credentials from the login page.

    Args:
        login_page: LoginPage instance from login_page fixture

    Returns:
        tuple: Tuple with (username, password)
    """
    with allure.step("Get user credentials"):
        credentials = login_page.get_credentials()
        allure.attach(
            credentials[0], name="Username", attachment_type=allure.attachment_type.TEXT
        )
    return credentials
