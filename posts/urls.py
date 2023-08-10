from django.urls import path
from .views import PostListCreateView, PostRetrieveUpdateView

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostRetrieveUpdateView.as_view(), name='post-retrieve-update'),
]