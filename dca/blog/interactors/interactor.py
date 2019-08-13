from ..dtos.dto import CreatePostDto
from ..repositories.repository import PostRepository
from ..entities.entity import PostEntity,UserEntity


# class UserInteractor:
#     def __init__(self):
#         self.repository = UserRepository()

# class GetUserInteractor:
#     pass




class PostInteractor:
    def __init__(self):
        self.repository = PostRepository()

class GetPostInteractor(PostInteractor):
    def __init__(self):
        super().__init__()

    def execute(self, post_id):
        return self.repository.get_post(post_id = post_id)

class CreatePostInteractor(PostInteractor):
    def __init__(self):
        super().__init__()

    def execute(self, post_dto: CreatePostDto ):

        post_entity = PostEntity(
            title=post_dto.title,
            content=post_dto.content,
            author=post_dto.author
        )

        return self.repository.create_post(entity=post_entity)

class GetPostListInteractor(PostInteractor):
    def __init__(self):
        super().__init__()

    def execute(self):
        return self.repository.get_post_list()