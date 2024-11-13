from django.urls import path
from . import views

urlpatterns = [
    path('', views.feed_view, name='feed'),
    path('post/', views.post_message, name='post_message'),
    path('delete/<int:message_id>/', views.delete_message, name='delete_message'),
    path('comment/<int:message_id>/', views.post_comment, name='post_comment'),
    path('like/message/<int:message_id>/', views.like_message, name='like_message'),
    path('like/comment/<int:comment_id>/', views.like_comment, name='like_comment'),
]
