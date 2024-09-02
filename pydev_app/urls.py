from django.urls import path
from .views import HomepageView, DatabaseOfQuestionsView, DetailsTopicView, DetailsLessonView, AdditionalResourceList, \
    AboutUsView, ApiEndpointsView, DetailsCategoryView

urlpatterns = [
    path('', HomepageView.as_view(), name='homepage'),
    path('database/', DatabaseOfQuestionsView.as_view(), name='database'),
    path('resources/', AdditionalResourceList.as_view(), name='resources'),
    path('about_us/', AboutUsView.as_view(), name='about'),
    path('api-endpoints/', ApiEndpointsView.as_view(), name='endpoints'),
    path('category/<slug:slug>/', DetailsCategoryView.as_view(), name='detail_category'),
    path('topic/<slug:slug>/', DetailsTopicView.as_view(), name='detail_topic'),
    path('lesson/<slug:slug>/', DetailsLessonView.as_view(), name='detail_lesson'),
]
