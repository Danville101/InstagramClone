from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status



CREATE_USER_URL = reverse('user:signup')

def create_user(**params):
         return get_user_model().objects.create_user(**params)
    
    
    

class PublicUser(TestCase):
     """Test User is Created Correctly"""
     
     def setUp(self):
          self.client = APIClient()
     
     
     def test_create_valid_user_successfully(self):
          
          payload={
               "username": "dontusename101",
               "email": "dontusereademail@gmail.com",
               "password": "dontuserealpassword101",
               "fullname": "Dontuse Name"
          }
          
      
          
          response = self.client.post(CREATE_USER_URL, payload)
          
          self.assertEqual(response.status_code, status.HTTP_201_CREATED)
          user = get_user_model().objects.get(**response.data)
          self.assertTrue(user.check_password(payload["password"]))
          self.assertNotIn("password", response.data)
          

