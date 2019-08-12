from dataclasses import dataclass
from datetime import datetime


@dataclass
class UserDto:
    id: int = None
    email: str = None
    username: str = None

@dataclass
class CreatePostDto:
    title: str = None
    content: str = None
    created_at: datetime = None
    updated_at: datetime = None
    author: UserDto = None

