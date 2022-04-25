
from django.urls import path

from . import views

app_name="post"

urlpatterns=[
     path("add_post/", views.PostIamge.as_view(), name="upload")
]



