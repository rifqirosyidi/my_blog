from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from . import views

app_name = 'my_blog'
urlpatterns = [
    path('', PostListView.as_view(), name="home"),
    path('user/<int:user_id>/posts/', UserPostListView.as_view(), name="user_post"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="detail"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="delete"),
    path('post/create/', PostCreateView.as_view(), name="create"),
]
