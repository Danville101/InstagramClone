from . import views
from django.urls import path


app_name = 'user'


urlpatterns = [
   path("register/", views.Register_User.as_view(), name="register")
]
