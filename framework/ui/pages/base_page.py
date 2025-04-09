from typing import Any, Callable
import logging
import time

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import (
    TimeoutException,
    StaleElementReferenceException,
    ElementClickInterceptedException,
)

logger = logging.getLogger(__name__)


class BasePage:
    """Base class for all page objects in the framework."""

    def __init__(
        self,
        driver: WebDriver,
        url: str | None = None,
        timeout: int = 10,
        polling_interval: float = 0.5,
        max_retry_attempts: int = 3,
    ) -> None:
        """
        Initialize the base page.

        Args:
            driver: WebDriver instance
            url: Optional URL to navigate to
            timeout: Default timeout in seconds for waits
            polling_interval: Interval between polling attempts in seconds
            max_retry_attempts: Maximum number of retry attempts for operations
        """
        self.driver = driver
        self.url = url
        self.timeout = timeout
        self.polling_interval = polling_interval
        self.max_retry_attempts = max_retry_attempts

    def open(self) -> None:
        """
        Open the page URL.

        Raises:
            AssertionError: If URL is not set
        """
        if not self.url:
            raise AssertionError("URL was not set for this page")

        logger.info(f"Navigating to: {self.url}")
        self.driver.get(self.url)

    def get_title(self) -> str:
        """Get the page title."""
        return self.driver.title

    def get_current_url(self) -> str:
        """Get the current URL."""
        return self.driver.current_url

    def find_element(
        self, locator: tuple[str, str], timeout: int | None = None
    ) -> WebElement:
        """
        Find an element with explicit wait.

        Args:
            locator: Tuple with By method and locator string
            timeout: Timeout in seconds (uses instance default if None)

        Returns:
            WebElement: Found element

        Raises:
            TimeoutException: If element is not found within timeout
        """
        timeout = timeout if timeout is not None else self.timeout
        try:
            logger.debug(f"Finding element: {locator}")
            return WebDriverWait(self.driver, timeout, self.polling_interval).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            logger.error(f"Element not found: {locator}")
            self._take_screenshot(f"element_not_found_{locator[1]}")
            raise

    def find_elements(
        self, locator: tuple[str, str], timeout: int | None = None
    ) -> list[WebElement]:
        """
        Find elements with explicit wait.

        Args:
            locator: Tuple with By method and locator string
            timeout: Timeout in seconds (uses instance default if None)

        Returns:
            list[WebElement]: List of found elements
        """
        timeout = timeout if timeout is not None else self.timeout
        try:
            logger.debug(f"Finding elements: {locator}")
            WebDriverWait(self.driver, timeout, self.polling_interval).until(
                lambda driver: len(driver.find_elements(*locator)) > 0
            )
            return self.driver.find_elements(*locator)
        except TimeoutException:
            logger.warning(f"No elements found: {locator}")
            return []

    def is_element_visible(
        self, locator: tuple[str, str], timeout: int | None = None
    ) -> bool:
        """
        Check if element is visible.

        Args:
            locator: Tuple with By method and locator string
            timeout: Timeout in seconds (uses instance default if None)

        Returns:
            bool: True if element is visible, False otherwise
        """
        timeout = timeout if timeout is not None else self.timeout
        try:
            WebDriverWait(self.driver, timeout, self.polling_interval).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def is_element_present(
        self, locator: tuple[str, str], timeout: int | None = None
    ) -> bool:
        """
        Check if element is present in DOM.

        Args:
            locator: Tuple with By method and locator string
            timeout: Timeout in seconds (uses instance default if None)

        Returns:
            bool: True if element is present, False otherwise
        """
        timeout = timeout if timeout is not None else self.timeout
        try:
            WebDriverWait(self.driver, timeout, self.polling_interval).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def wait_for_element_clickable(
        self, locator: tuple[str, str], timeout: int | None = None
    ) -> WebElement:
        """
        Wait for element to be clickable.

        Args:
            locator: Tuple with By method and locator string
            timeout: Timeout in seconds (uses instance default if None)

        Returns:
            WebElement: Clickable element

        Raises:
            TimeoutException: If element is not clickable within timeout
        """
        timeout = timeout if timeout is not None else self.timeout
        try:
            logger.debug(f"Waiting for element to be clickable: {locator}")
            return WebDriverWait(self.driver, timeout, self.polling_interval).until(
                EC.element_to_be_clickable(locator)
            )
        except TimeoutException:
            logger.error(f"Element not clickable: {locator}")
            self._take_screenshot(f"element_not_clickable_{locator[1]}")
            raise

    def click_element(
        self,
        locator: tuple[str, str],
        timeout: int | None = None,
        retry_on_stale: bool = True,
    ) -> None:
        """
        Click on element with retry.

        Args:
            locator: Tuple with By method and locator string
            timeout: Timeout in seconds (uses instance default if None)
            retry_on_stale: Whether to retry on StaleElementReferenceException

        Raises:
            Exception: If clicking fails after retries
        """
        timeout = timeout if timeout is not None else self.timeout
        retry_count = 0

        while retry_count < self.max_retry_attempts:
            try:
                element = self.wait_for_element_clickable(locator, timeout)
                logger.debug(f"Clicking element: {locator}")
                element.click()
                return
            except (
                StaleElementReferenceException,
                ElementClickInterceptedException,
            ) as e:
                if not retry_on_stale or retry_count >= self.max_retry_attempts - 1:
                    logger.error(
                        f"Failed to click element after {retry_count + 1} attempts: {locator}"
                    )
                    self._take_screenshot(f"click_failed_{locator[1]}")
                    raise e

                logger.warning(f"Retrying click due to {e.__class__.__name__}")
                retry_count += 1
                time.sleep(self.polling_interval)

    def input_text(
        self,
        locator: tuple[str, str],
        text: str,
        clear_first: bool = True,
        timeout: int | None = None,
    ) -> None:
        """
        Input text into an element.

        Args:
            locator: Tuple with By method and locator string
            text: Text to input
            clear_first: Whether to clear the field first
            timeout: Timeout in seconds (uses instance default if None)
        """
        timeout = timeout if timeout is not None else self.timeout
        element = self.find_element(locator, timeout)

        if clear_first:
            element.clear()

        logger.debug(f"Inputting text into element: {locator}")
        element.send_keys(text)

    def get_text(self, locator: tuple[str, str], timeout: int | None = None) -> str:
        """
        Get text from element.

        Args:
            locator: Tuple with By method and locator string
            timeout: Timeout in seconds (uses instance default if None)

        Returns:
            str: Element text
        """
        timeout = timeout if timeout is not None else self.timeout
        element = self.find_element(locator, timeout)
        return element.text

    def get_attribute(
        self, locator: tuple[str, str], attribute: str, timeout: int | None = None
    ) -> str | None:
        """
        Get attribute value from element.

        Args:
            locator: Tuple with By method and locator string
            attribute: Attribute name
            timeout: Timeout in seconds (uses instance default if None)

        Returns:
            str | None: Attribute value or None if not present
        """
        timeout = timeout if timeout is not None else self.timeout
        element = self.find_element(locator, timeout)
        return element.get_attribute(attribute)

    def wait_for_condition(
        self,
        condition: Callable[[WebDriver], Any],
        timeout: int | None = None,
        message: str = "",
    ) -> Any:
        """
        Wait for a custom condition.

        Args:
            condition: Function that takes a WebDriver and returns a value
            timeout: Timeout in seconds (uses instance default if None)
            message: Error message for TimeoutException

        Returns:
            Any: The return value of the condition function

        Raises:
            TimeoutException: If condition is not met within timeout
        """
        timeout = timeout if timeout is not None else self.timeout
        return WebDriverWait(self.driver, timeout, self.polling_interval).until(
            condition, message
        )

    def scroll_to_element(
        self, locator: tuple[str, str], timeout: int | None = None
    ) -> None:
        """
        Scroll to element.

        Args:
            locator: Tuple with By method and locator string
            timeout: Timeout in seconds (uses instance default if None)
        """
        timeout = timeout if timeout is not None else self.timeout
        element = self.find_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        # Small pause to allow the page to settle after scrolling
        time.sleep(0.5)

    def hover_over_element(
        self, locator: tuple[str, str], timeout: int | None = None
    ) -> None:
        """
        Hover over element.

        Args:
            locator: Tuple with By method and locator string
            timeout: Timeout in seconds (uses instance default if None)
        """
        timeout = timeout if timeout is not None else self.timeout
        element = self.find_element(locator, timeout)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def switch_to_iframe(
        self, locator: tuple[str, str], timeout: int | None = None
    ) -> None:
        """
        Switch to iframe.

        Args:
            locator: Tuple with By method and locator string
            timeout: Timeout in seconds (uses instance default if None)

        Raises:
            TimeoutException: If iframe is not found within timeout
        """
        timeout = timeout if timeout is not None else self.timeout
        try:
            logger.debug(f"Switching to iframe: {locator}")
            WebDriverWait(self.driver, timeout, self.polling_interval).until(
                EC.frame_to_be_available_and_switch_to_it(locator)
            )
        except TimeoutException:
            logger.error(f"Iframe not available: {locator}")
            self._take_screenshot("iframe_not_available")
            raise

    def switch_to_default_content(self) -> None:
        """Switch back to default content from iframe."""
        self.driver.switch_to.default_content()

    def accept_alert(self, timeout: int | None = None) -> None:
        """
        Accept alert.

        Args:
            timeout: Timeout in seconds (uses instance default if None)

        Raises:
            TimeoutException: If alert is not present within timeout
        """
        timeout = timeout if timeout is not None else self.timeout
        try:
            WebDriverWait(self.driver, timeout, self.polling_interval).until(
                EC.alert_is_present()
            )
            self.driver.switch_to.alert.accept()
        except TimeoutException:
            logger.error("Alert not present")
            self._take_screenshot("alert_not_present")
            raise

    def dismiss_alert(self, timeout: int | None = None) -> None:
        """
        Dismiss alert.

        Args:
            timeout: Timeout in seconds (uses instance default if None)

        Raises:
            TimeoutException: If alert is not present within timeout
        """
        timeout = timeout if timeout is not None else self.timeout
        try:
            WebDriverWait(self.driver, timeout, self.polling_interval).until(
                EC.alert_is_present()
            )
            self.driver.switch_to.alert.dismiss()
        except TimeoutException:
            logger.error("Alert not present")
            self._take_screenshot("alert_not_present")
            raise

    def _take_screenshot(self, name: str) -> None:
        """
        Take a screenshot and save it.

        Args:
            name: Screenshot name
        """
        try:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            filename = f"screenshot_{name}_{timestamp}.png"
            self.driver.save_screenshot(filename)
            logger.info(f"Screenshot saved: {filename}")
        except Exception as e:
            logger.error(f"Failed to take screenshot: {str(e)}")

    def wait_for_page_load(self, timeout: int | None = None) -> None:
        """
        Wait for page to load completely.

        Args:
            timeout: Timeout in seconds (uses instance default if None)
        """
        timeout = timeout if timeout is not None else self.timeout
        self.wait_for_condition(
            lambda d: d.execute_script("return document.readyState") == "complete",
            timeout,
            "Page did not load completely",
        )

    def wait_for_element_to_disappear(
        self, locator: tuple[str, str], timeout: int | None = None
    ) -> None:
        """
        Wait for element to disappear.

        Args:
            locator: Tuple with By method and locator string
            timeout: Timeout in seconds (uses instance default if None)
        """
        timeout = timeout if timeout is not None else self.timeout
        logger.debug(f"Waiting for element to disappear: {locator}")
        WebDriverWait(self.driver, timeout, self.polling_interval).until_not(
            EC.visibility_of_element_located(locator)
        )
