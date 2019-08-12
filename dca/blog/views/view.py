from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from ..serializers.serializer import GetPostRequestSerializer,UserSerializer
from ..interactors.interactor import GetPostInteractor
from django.forms.models import model_to_dict


class Post(APIView):

    def get(self, request: Request, post_id: int):
        post = GetPostInteractor().execute(post_id=post_id)
        serializer = GetPostRequestSerializer(post)
        if post:
            return Response(data =serializer.data ,status=status.HTTP_200_OK)

        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    # def post(self ,request: Request , format=None):
    #     pass


# class PostList(APIView):
#     def get(self , request: Request, format=None):
#         pass