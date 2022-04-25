from . import views
from django.urls import path
from rest_framework_simplejwt.views import   TokenObtainPairView, TokenRefreshView



app_name = 'user'


urlpatterns = [
   path("signup/", views.Register_User.as_view(), name="signup"),
   path('login/', TokenObtainPairView.as_view(), name='login'),
   path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   path("", views.Home.as_view(), name="home"),
]
