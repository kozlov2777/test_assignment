import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    """
    Fixture that provides a Chrome WebDriver instance.

    Returns:
        WebDriver: Chrome browser instance
    """
    with allure.step("Configure Chrome WebDriver"):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--headless")
        chrome_options.add_experimental_option(
            "prefs",
            {
                "profile.password_manager_leak_detection": False,
                "profile.password_manager_enabled": False,
            },
        )
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

    with allure.step("Initialize Chrome WebDriver"):
        driver = webdriver.Chrome(options=chrome_options)
        allure.attach(
            "Chrome WebDriver initialized",
            name="Browser",
            attachment_type=allure.attachment_type.TEXT,
        )

    yield driver

    with allure.step("Close browser"):
        driver.quit()
