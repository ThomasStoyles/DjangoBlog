from django.urls import path
from . import views
from .views import (
    PostListView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    about,
    contact,
    register,
)

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', views.post_detail, name='post-detail'),  # Use only your function-based view
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', about, name='blog-about'),
    path('contact/', contact, name='blog-contact'),
    path('register/', register, name='register'),
    path('category/<int:category_id>/', views.category_posts, name='category-posts'),
    path('category/<str:category_name>/', views.PostsByCategoryView.as_view(), name='posts-by-category'),

]
