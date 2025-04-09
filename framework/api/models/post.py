from pydantic import BaseModel, Field, ConfigDict
from typing import Optional


class Post(BaseModel):
    """
    Model representing a post from JSONPlaceholder API.

    Attributes:
        user_id: The ID of the user who created the post
        id: The ID of the post
        title: The title of the post
        body: The content of the post
    """

    model_config = ConfigDict(
        populate_by_name=True,
        extra="forbid",
        strict=True,
    )

    user_id: int = Field(
        alias="userId", description="ID of the user who created the post"
    )
    id: int = Field(description="Unique identifier for the post")
    title: str = Field(description="Title of the post")
    body: str = Field(description="Content of the post")
