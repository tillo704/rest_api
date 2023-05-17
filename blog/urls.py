from django.contrib import admin
from django.urls import path, include
from .views import category_list, category_detail,post_list,post_detail

urlpatterns = [
    path('cats/',category_list,name="api_main"),
    path('cat/<int:pk>/',category_detail,name='category_detail'),
    path('posts/',post_list,name='post_list'),
    path('post/<int:pk>/',post_detail,name='post_detail'),
]