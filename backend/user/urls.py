from . import views
from django.urls import path


app_name = 'user'


urlpatterns = [
   path("signup/", views.Register_User.as_view(), name="signup")
]
