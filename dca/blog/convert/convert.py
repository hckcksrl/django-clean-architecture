from ..models.model import Post
from ..entities.entity import PostEntity
from django.forms.models import model_to_dict
from django.contrib.auth.models import User

class PostConvert:
    def post_model_to_entity(self, model:Post):
        entity = PostEntity(**model_to_dict(model))
        return entity