from rest_framework import serializers
from ..models.model import Post
from django.contrib.auth.models import User

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)

    # def to_representation(self, instance):
    #     return{
    #         'id':instance.id,
    #         'email':instance.email,
    #         'username':instance.username
    #     }



class GetPostRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    title = serializers.CharField(required=True)
    content = serializers.CharField(required=True)
    created_at = serializers.DateTimeField(required=True)
    updated_at = serializers.DateTimeField(required=True)
    author = UserSerializer(required=True)

    # def to_representation(self, instance):
    #     return{
    #         'id':instance.id,
    #         'title':instance.title,
    #         'content':instance.content,
    #         'created_at':instance.created_at,
    #         'updated_at':instance.updated_at,
    #         'author':instance.author
    #     }

class CreatePostSerializer(serializers.BaseSerializer):
    title = serializers.CharField
    content = serializers.CharField
    created_at = serializers.DateTimeField
    updated_at = serializers.DateTimeField
    author = UserSerializer

