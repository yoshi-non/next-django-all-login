from django.urls import path

from .views import PostList, PostDetail

urlpatterns = [
    path('posts/<str:pk>/', PostDetail.as_view()),
    path('posts/', PostList.as_view()),
]