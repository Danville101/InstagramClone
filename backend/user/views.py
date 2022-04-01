from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from user.serializers import UserProfileSerializer
from user.models import UserProfile
# Create your views here.




class Register_User(APIView):
     
     def post(self, request, format=None):
          serializer = UserProfileSerializer(data = request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data, status= status.HTTP_201_CREATED)
          else:
               return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
     
     
     
     def get(self, request, format=None):
          users = UserProfile.objects.all()
          serializer = UserProfileSerializer(users, many=True)
          return Response(serializer.data,)


class Home(APIView):
     
     pass
     