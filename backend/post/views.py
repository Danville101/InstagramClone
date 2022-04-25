from django.shortcuts import render
from rest_framework.views import APIView  
from .serializer import PostSerailizer
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import permissions

class PostIamge(APIView):
     permission_classes = [permissions.IsAuthenticated]
     parser_class = [MultiPartParser, FormParser]
     
     
     def post(self, request, format=None):
          
          serializer = PostSerailizer(data = request.data)
          if serializer.is_valid():
               serializer.save(user=self.request.user)
               return Response(serializer.data, status= status.HTTP_201_CREATED)
          else:
               return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
     
     def get(self, request, format=None):
          post = Post.objects.all()
          serailizer= PostSerailizer(post, many=True)
          return Response(serailizer.data,)


#class PostIamge(APIView):
#    serializer_class = PostSerailizer
#
#    def post(self, request, *args, **kwargs):
#      file = request.data
#      image = Post.objects.create(picture=file)
#      return Response(image.data,status=201)