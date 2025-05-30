import random
from http import HTTPStatus

import allure
import pytest
import pytest_check as check
from pydantic import ValidationError

from framework.api.models.post import Post


@pytest.mark.api
@allure.parent_suite("API Tests")
@allure.suite("JSONPlaceholder API")
@allure.feature("Posts API")
class TestJsonPlaceholder:

    @allure.story("Successful post retrieval")
    @allure.title("Verify successful retrieval of a post by ID")
    @allure.description(
        """
        This test verifies that the API correctly returns a post when requested by ID:
        1. Sends a GET request to retrieve a post by ID
        2. Verifies the status code is 200 OK
        3. Validates that the response contains the 'title' field as a string
        4. Validates the complete response schema using Pydantic model
        """
    )
    def test_get_post_json_placeholder_api(self, json_placeholder_client):
        post_id = random.randint(1, 50)

        with allure.step(f"Get post with ID {post_id}"):
            response = json_placeholder_client.get_post(post_id)

        with allure.step("Verify the response status code is 200"):
            check.equal(response.status_code, HTTPStatus.OK)

        with allure.step("Get response body"):
            try:
                data = response.json()
            except Exception as e:
                allure.attach(
                    f"Failed to parse response as JSON: {str(e)}\nResponse text: {response.text}",
                    name="JSON Parsing Error",
                    attachment_type=allure.attachment_type.TEXT,
                )
                pytest.fail(f"Failed to parse response as JSON: {e}")

        with allure.step("Validate response schema using Pydantic model"):
            try:
                post = Post.model_validate(data)

                allure.attach(
                    post.model_dump_json(indent=2),
                    name="Validated Post Object",
                    attachment_type=allure.attachment_type.JSON,
                )
            except ValidationError as e:
                allure.attach(
                    f"Validation Error: {str(e)}\n\nData: {data}",
                    name="Schema Validation Error",
                    attachment_type=allure.attachment_type.TEXT,
                )
                pytest.fail(f"Response data failed schema validation: {e}")

    @allure.story("Error handling")
    @allure.title("Verify 404 response when requesting a non-existent post")
    @allure.description(
        """
        This test verifies that the API correctly handles requests for non-existent posts:
        1. Sends a GET request with an ID that doesn't exist
        2. Verifies the status code is 404 Not Found
        3. Validates that the response body is an empty JSON object
        """
    )
    def test_get_nonexistent_post_json_placeholder_api(self, json_placeholder_client):
        non_existent_id = random.randint(101, 9999)

        with allure.step(f"Get post with non-existent ID {non_existent_id}"):
            response = json_placeholder_client.get_post(non_existent_id)

        with allure.step("Verify the response status code is 404"):
            check.equal(response.status_code, HTTPStatus.NOT_FOUND)

        with allure.step("Verify the response body is empty JSON"):
            try:
                data = response.json()
            except ValueError as e:
                allure.attach(
                    f"Failed to parse response as JSON: {str(e)}\nResponse text: {response.text}",
                    name="JSON Parsing Error",
                    attachment_type=allure.attachment_type.TEXT,
                )
                pytest.fail(f"Failed to parse response as JSON: {e}")

        check.equal(data, {}, f"Expected empty JSON object, got {data}")
