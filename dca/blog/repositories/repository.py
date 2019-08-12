from ..entities.entity import PostEntity
import abc
from ..models.model import Post
from ..convert.convert import PostConvert
from ..serializers.serializer import GetPostRequestSerializer
from django.contrib.auth.models import User

class PostABCRepository:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_post(self, post_id:int):
        pass


class PostRepository(PostABCRepository):
    def __init__(self):
        self.convert = PostConvert()

    def get_post(self, post_id:int):
        post = Post.objects.get(id=post_id)
        if post is None :
            raise Exception('Not Found Error')
        # return self.convert.post_model_to_entity(model=post)
        return post