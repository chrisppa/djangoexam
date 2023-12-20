from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView


urlpatterns = [
    path('home/', views.form1),
    path('hello/', PostListView.as_view(), name='hello'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create')
]
