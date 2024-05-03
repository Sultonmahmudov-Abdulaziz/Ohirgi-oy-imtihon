from django.urls import path
from .views import (
    LoginApiView,
    RegisterApiView,
    AllUserView,
    PostApiView,
    PostDeleteApiView,
    AllPostsApiView,
    CreatePostApiView,
    AddCommentAPIView,
    GetAllCommentAPIView,
    AddLikesAPIView,
    UsersWhoLikedPostView
)



app_name = 'users'

urlpatterns = [
    path('log-in/', LoginApiView.as_view(), name='login'),
    path('register/', RegisterApiView.as_view(), name='register'),
    path('all-users/', AllUserView.as_view(), name='all_user'),
    path('post/<int:id>/', PostApiView.as_view(), name='post'),
    path('create-post/', CreatePostApiView.as_view(), name='create_post'),
    path('post_update/<int:id>/', PostApiView.as_view(), name='post_update'),
    path('all-posts/', AllPostsApiView.as_view(), name='all_posts'),
    path('post_delete/<int:id>/', PostDeleteApiView.as_view(), name='post_delete'),
    path('add-comment/<int:id>/', AddCommentAPIView.as_view(), name='add_comment'),
    path('all-comments/<int:id>/', GetAllCommentAPIView.as_view(), name='all_comments'),
    path('add-likes/<int:id>/', AddLikesAPIView.as_view(), name='add_likes'),
    path('all-liked-post/<int:id>/', UsersWhoLikedPostView.as_view(), name='users_who_liked_post')
]