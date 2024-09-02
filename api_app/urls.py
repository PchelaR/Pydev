from django.urls import path

from .views import UserCreateView, LessonListView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'api'

urlpatterns = [
    path('api/register/', UserCreateView.as_view(), name='user-register'),
    path('api/lessons/', LessonListView.as_view(), name='lesson-list'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]