from .import views
from django.urls import path

urlpatterns = [

    path("", views.index),
    path("addPost/", views.addPost, name='addPost'),
    path('readPost/<int:id>', views.detailedBlog, name='readPost'),
    path('likePost/<int:id>', views.likePost, name='likePost'),
]
