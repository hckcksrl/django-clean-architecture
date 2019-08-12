from dataclasses import dataclass
from datetime import datetime

@dataclass
class UserEntity:
    id: int = None
    email: str = None
    password: str = None
    username: str = None
    first_name: str = None
    last_name: str = None
    is_staff: bool = False
    is_superuser: bool = False
    is_active: bool = True
    last_login: datetime = None
    date_joined: datetime = None

@dataclass
class PostEntity:
    id: int = None
    title: str = None
    content: str = None
    created_at: datetime = None
    updated_at: datetime = None
    author: UserEntity = None


