from django.urls import path
from . import views
from .views import (PostListView, PostDetailView, PostCreateView,
                    PostUpdateView, PostDeleteView, UserPostListView,
                    SearchListView
                    # TypePostListView
                    # PostCommentView
                    )


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/posts/<str:username>',
         UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(),  name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('search/', SearchListView.as_view(),  name='post-search'),
    path('about/', views.about, name='blog-about'),

]

# path('post/morepost',
#      TypePostListView.as_view(), name='post-types'),
