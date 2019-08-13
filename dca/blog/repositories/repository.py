import abc
from ..models.model import Post
from ..convert.convert import PostConvert
from ..entities.entity import PostEntity
from django.contrib.auth.models import User
# from ..serializers.serializer import GetPostRequestSerializer
# from django.contrib.auth.models import User

class PostABCRepository:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_post(self, post_id:int):
        pass

    @abc.abstractmethod
    def create_post(self, entity:PostEntity):
        pass

    def get_post_list(self):
        pass

    def delete_post(self, post_int:int):
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

    def create_post(self, entity:PostEntity):
        user = User.objects.get(username=entity.author['username'])
        entity.author = user
        post_dict = self.convert.post_entity_to_dict(entity=entity)
        post = Post(**post_dict).save()
        return post

    def get_post_list(self):
        post = Post.objects.all()
        if post is None:
            raise Exception('Not Found Error')

        return post

    def delete_post(self, post_id:int):
        post = self.get_post(post_id=post_id)
        if post is None :
            return False
        post.delete()
        return True