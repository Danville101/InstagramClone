from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from post.models import Post
from rest_framework.test import APIClient
from rest_framework import status
import tempfile
import os
from PIL import Image
import io

POST_URL = reverse("post:upload")

def sample_post(user, **params):
        return Post.objects.create(user=user, **params)


class UploadTest(TestCase):
     
      def setUp(self):
         self.client=APIClient()
         self.user = get_user_model().objects.create_user(
              username= "dontusename101",
               email= "dontusereademail@gmail.com",
               fullname= "Dontuse Name",
               password= "dontuserealpassword101",
               )
         self.client.force_authenticate(self.user)
         self.upload = sample_post(user=self.user)
         
      def tearDown(self):
         self.upload.delete()
      
        
      def test_uploading_image(self):
          with tempfile.NamedTemporaryFile(suffix=".jpg") as ntf:
            img = Image.new("RGB",(10,10), color= "red")
            img.save(ntf, format="JPEG")
            ntf.seek(0)
            res = self.client.post(POST_URL,{ "user":self.user,"picture":ntf}, format="multipart")
                  
            self.assertEqual(res.status_code, status.HTTP_201_CREATED)
            self.assertIn("picture",res.data)
            self.assertTrue(os.path.exists(self.post.picture.path))
   