import pytest

from framework.api.clients.json_placeholder_client import JsonPlaceholderClient


@pytest.fixture
def json_placeholder_client():
    """
    Fixture that provides a JsonPlaceholderClient instance.

    Returns:
        JsonPlaceholderClient: Initialized API client for JSONPlaceholder service
    """
    with JsonPlaceholderClient() as client:
        yield client
