import httpx
import allure
from typing import Union


class BaseClient(httpx.Client):
    """
    Enhanced version of httpx.Client with Allure integration for request and response logging.
    """

    def request(
        self, method: str, url: Union[str, httpx.URL], **kwargs
    ) -> httpx.Response:
        """
        Overridden request method with Allure logging capabilities.

        Args:
            method: HTTP method to use
            url: URL to request
            **kwargs: Additional arguments to pass to the request

        Returns:
            httpx.Response object
        """
        with allure.step(f"{method} {url}"):
            allure.attach(
                f"URL: {url}\n"
                f"Method: {method}\n"
                f"Params: {kwargs.get('params')}\n"
                f"JSON: {kwargs.get('json')}\n"
                f"Headers: {kwargs.get('headers')}",
                name="Request",
                attachment_type=allure.attachment_type.TEXT,
            )

            response = super().request(method, url, **kwargs)

            allure.attach(
                f"Status Code: {response.status_code}\n"
                f"Response Time: {response.elapsed.total_seconds()}s",
                name="Response Info",
                attachment_type=allure.attachment_type.TEXT,
            )

            try:
                response_json = response.json()
                allure.attach(
                    str(response_json),
                    name="Response Body (JSON)",
                    attachment_type=allure.attachment_type.JSON,
                )
            except Exception:
                allure.attach(
                    response.text,
                    name="Response Body (Text)",
                    attachment_type=allure.attachment_type.TEXT,
                )

            return response
