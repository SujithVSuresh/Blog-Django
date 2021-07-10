from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="blog-home" ),
    path('about/', views.about, name="blog-about" ),
    path('create-post/<str:pk>/', views.createPost, name="create-post"),
    path('my-post/', views.myPost, name="my-post"),
    path('update-post/<str:pk>/', views.updatePost, name="update-post"),
    path('delete-post/<str:pk>/', views.deletePost, name="delete-post"),

]