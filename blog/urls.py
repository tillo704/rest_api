from django.contrib import admin
from django.urls import path, include
from .views import category_list, category_detail,category_create,category_delete,PostListCreateAPIView,PostDetailUpdateDeleteAPIView

urlpatterns = [
    path('cats/',category_list,name="api_main"),
    path('cat/<slug:slug>/',category_detail,name='category_detail'),    
    path('posts/',PostListCreateAPIView.as_view(),name='post_list_create_view'),
    path('cat/delete/<slug:slug>/',category_delete,name='category_delete'),
    path('post/<slug:slug>/',PostDetailUpdateDeleteAPIView.as_view(),name='PostDetailUpdateDeleteAPIView'),
    path('create/cat/', category_create,name='category_create'),
]