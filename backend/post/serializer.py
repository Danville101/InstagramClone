from dataclasses import fields
from rest_framework import serializers

from .models import Post, Comments, Likes



class CommentsSeraializer(serializers.ModelSerializer):
     
     class Meta:
          model = Comments
          fields="__all__"
          read_only_fields = ("user",)

class LikesSerializer(serializers.ModelSerializer):
     
     class Meta:
          model = Likes
          fields= "__all__"
          read_only_fields = ("user",)


class PostSerailizer(serializers.ModelSerializer):
     post_comments = CommentsSeraializer(many= True, read_only=True)
     post_likes = LikesSerializer(many= True, read_only=True)
     
     class Meta:
          model= Post
          fields="__all__"
          read_only_fields = ("user",)

