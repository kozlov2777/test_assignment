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
        """
        Retrieve a post by its ID.

        Args:
            post_id: The ID of the post to retrieve

        Returns:
            httpx.Response: The HTTP response containing the post data
        """
        return self.get(f"/posts/{post_id}")
