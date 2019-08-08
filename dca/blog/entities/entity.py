from dataclasses import dataclass
from datetime import datetime
from django.contrib.auth.models import User

@dataclass()
class PostEntity:
    title: str = None
    content: str = None
    created_at: datetime = None
    updated_at: datetime = None
    author: User = None


