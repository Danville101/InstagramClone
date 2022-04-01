from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status



CREATE_USER_URL = reverse('user:signup')

LOGIN_URL = reverse('user:login')

HOME_URL = reverse('user:home')

def create_user(**params):
         return get_user_model().objects.create_user(**params)
    
    
    

class CreateUser(TestCase):
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
          


class LoginTestCase(TestCase):
     """Test if user can log in and is authenticated"""
     
     def setUp(self):
          self.user = create_user(
              username= "dontusename101",
               email= "dontusereademail@gmail.com",
               password= "dontuserealpassword101",
               fullname= "Dontuse Name"
          )
          self.client = APIClient
          self.client.force_authenticate(user= self.user)
     
     
     def test_login_access_token(self):
          
          response = self.client.post(LOGIN_URL)
          
          self.assertIn("access", response.data)
          
     
     
     def test_user_can_asscees_account(self):
          
          response = self.client.get(HOME_URL)
          
          self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
          
          
          
          
          
     
     
