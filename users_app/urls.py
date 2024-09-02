from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import UserRegisterView, UserLoginView, SuccessView

app_name = 'users'

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('register/success/', SuccessView.as_view(), name='register_success'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
