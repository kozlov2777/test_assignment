import httpx

from framework.api.clients.base_client import BaseClient


class JsonPlaceholderClient(BaseClient):
    """
    Client for interacting with JSONPlaceholder API.
    """

    def __init__(self, **kwargs):
        super().__init__(
            base_url="https://jsonplaceholder.typicode.com", timeout=5.0, **kwargs
        )

    def get_post(self, post_id: int) -> httpx.Response:
        return self.get(f"/posts/{post_id}")
