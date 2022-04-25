from distutils.command.upload import upload
from django.db import models
from django.conf import settings
import uuid
import os 


def image_file_path(instance, filename):
        ext = filename.split(".")[-1]
        filename = f'{uuid.uuid4()}.{ext}'
        
        return f'uploads/post/{filename}'

class Post(models.Model):
     user = models.ForeignKey(settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,)
     picture = models.ImageField(upload_to=image_file_path)
     
     def __str__(self) -> str:
        file = self.user + self.picture
        return file

class Comments(models.Model):
   text = models.CharField(default= "",max_length=10000, null=True)
   post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_comments")
   user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
class Likes(models.Model):
   
   post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_likes")
   user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE )
   amount = models.PositiveIntegerField(default=0 , null=True)
   
   