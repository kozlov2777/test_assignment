import pytest

from framework.api.clients.json_placeholder_client import JsonPlaceholderClient


@pytest.fixture
def jsonplaceholder_client():
    with JsonPlaceholderClient() as client:
        yield client
