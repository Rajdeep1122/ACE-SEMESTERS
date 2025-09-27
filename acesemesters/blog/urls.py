from django.urls import path
from .views import (
    HomeView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    category_view,
    SignUpView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('category/<str:category_name>/', category_view, name='category'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
