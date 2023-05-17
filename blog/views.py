from datetime import datetime
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_201_CREATED,HTTP_204_NO_CONTENT
from .models import Category,Post
from django.forms.models import model_to_dict

@api_view(http_method_names=['GET','POST','DELETE'])
def category_list(request: Request):
    # print(request.method,'METHOD')
    # print(request.user,"USER")
    # print(request.content_type,'CONTENT_TYPS')
    # print(request.query_params,'PARAMS')
    
    

    # if request.method == "POST":
    #     print(request.data,'DATA')
            
    #     name= request.data.get("name")
    #     age = request.data.get('age')
    #     cuerrent_year = datetime.now().year
    #     b_year = cuerrent_year-age
    #     return Response(data={"name":name.upper(),"b_year":b_year})
    # elif request.method=="DELETE":
    #     return JsonResponse(data={},status=HTTP_204_NO_CONTENT)

    categories = Category.objects.all().values()    
    return Response(data=list(categories))


@api_view(['GET',])
def category_detail(request: Request,pk:int):
    category = Category.objects.filter(pk=pk).values()
    return Response(data=list(category))


@api_view(http_method_names=['GET','POST','DELETE'])
def post_list(request: Request):
    posts = Post.objects.all().values()    
    return Response(data=list(posts))




@api_view(['GET',])
def post_detail(request: Request,pk:int):
    post = Post.objects.filter(pk=pk).values()
    return Response(data=list(post))