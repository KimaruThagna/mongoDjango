from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
# Create your views here.
class AllPosts (APIView):
    def get(self, request):
        if request.method == 'GET':
            title = request.GET.get('title')# if we wish to filter by title
            if title:
                posts = BlogPost.objects.filter(title__contains=title)
            else: # no filter provided hence retrieve all
                posts = BlogPost.objects.all()
            #retrieve all blog posts
            all_posts = BlogPostSerializer(posts, many=True).data
            response = {'results': all_posts}
            return Response(response)

    def post(self, request, format=None):
        serializer = BlogPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)