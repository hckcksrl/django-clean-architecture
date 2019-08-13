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
    author: UserDto = None


@dataclass
class PostListDto:
    offset: int = None
    limit: int = None