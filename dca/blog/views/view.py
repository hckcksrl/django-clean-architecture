from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from ..serializers.serializer import GetPostRequestSerializer,UserSerializer,CreatePostSerializer
from ..interactors.interactor import GetPostInteractor,CreatePostInteractor
from ..dtos.dto import CreatePostDto,PostListDto

class Post(APIView):

    def get(self, request: Request, post_id: int):
        post = GetPostInteractor().execute(post_id=post_id)
        serializer = GetPostRequestSerializer(post)
        if post is None:
           return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class Blog(APIView):

    def get(self, request: Request):
        print(request.GET['limit'])
        return Response(status=status.HTTP_200_OK)

    def post(self ,request: Request ):
        serializer = CreatePostSerializer(data=request.data)
        if serializer.is_valid() is False:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        dto = CreatePostDto(**serializer.data)
        post = CreatePostInteractor().execute(post_dto=dto)
        return Response(status=status.HTTP_201_CREATED, data = post)


# class PostList(APIView):
#     def get(self , request: Request, format=None):
#         pass