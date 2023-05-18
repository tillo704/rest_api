from datetime import datetime
from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_201_CREATED,HTTP_204_NO_CONTENT,HTTP_400_BAD_REQUEST,HTTP_200_OK
from .models import Category,Post
from django.forms.models import model_to_dict
from .serializers import CaretegorySerializer,PostSeralizer
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView


@api_view(http_method_names=["GET",'POST'])
def category_create(request: Request):
    serializer = CaretegorySerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=HTTP_201_CREATED)

@api_view(http_method_names=['GET','POST','DELETE'])
def category_list(request: Request):
   serializer = CaretegorySerializer(instance=Category.objects.all(),many=True)
   return Response(data=serializer.data)




@api_view(['GET',"PATCH", "PUT"])
def category_detail(request: Request,slug: str):
    category = get_object_or_404(Category,slug=slug)
    if request.method == "PUT":
        serializer = CaretegorySerializer(instance=category, data= request.data)
        serializer.is_valid(raise_exception=True)
        serializer.update(instanece=category, validated_data=serializer.validated_data)
        return Response(data=serializer.data)

    elif request.method == "PATCH":
        serializer = CaretegorySerializer(instance=category, data= request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.update(instanece=category, validated_data=serializer.validated_data)
        return Response(data=serializer.data)
    
    else:
        category = get_object_or_404(Category, slug=slug)
        serializer = CaretegorySerializer(instance=category)
        return Response(data=serializer.data)
    

@api_view(['DELETE'])
def category_delete(request: Request, slug: str):
    category = get_object_or_404(Category, slug=slug)
    category.delete()
    return Response(data={}, status=HTTP_204_NO_CONTENT)




class PostListCreateAPIView(GenericAPIView):
    queryset =Post.objects.all()
    serializer_class =PostSeralizer

    def get(self, request):
       
        serializer = self.serializer_class(instance=self.get_queryset(), many= True)
        return Response(data=serializer.data,status=HTTP_200_OK)
    
    def post(self, request):
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(data=serializer.data, status= HTTP_201_CREATED)


class PostDetailUpdateDeleteAPIView(GenericAPIView):
    queryset =Post.objects.all()
    serializer_class =PostSeralizer
    lookup_field = "slug"

    def get(self, request, slug):
        post= get_object_or_404(Post,slug=slug)
        serializer = PostSeralizer(instance=post)
        return Response(data=serializer.data,status=HTTP_200_OK)
    

    def put(self, request, slug):
        post= get_object_or_404(Post,slug=slug)
        serializer = PostSeralizer(instance=post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=HTTP_200_OK)

    def patch(self, request, slug):
        post= get_object_or_404(Post,slug=slug)
        serializer = PostSeralizer(instance=post,data=request.data, partial = True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=HTTP_200_OK)
    
    def delete(self, request, slug):
        post= get_object_or_404(Post,slug=slug)
        post.delete()
        return Response(data={},status=HTTP_204_NO_CONTENT)
        


# @api_view(http_method_names=['GET','POST'])
# def post_list_create_view(request: Request):
#     if request.method == "POST":
    #     serializer = PostSeralizer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(data=serializer.data, status= HTTP_201_CREATED)
    # posts = Post.objects.all()
    # serializer = PostSeralizer(instance=posts, many= True)
    # return Response(data=serializer.data,status=HTTP_200_OK)
    

# @api_view(['GET','PUT',"PATCH" ,'DELETE'])
# def post_detail(request: Request,pk:int):
#     post = Post.objects.filter(pk=pk).values()
#     return Response(data=list(post))