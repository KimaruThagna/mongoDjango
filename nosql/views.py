from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
# Create your views here.
# statment = request.GET.get('statement')
class AllPosts (APIView):
    def get(self, request):
        if request.method == 'GET':
            title = request.GET.get('title')
            if title:
                posts = BlogPost.objects.filter(title__contains=title)
            else:
                posts = BlogPost.objects.all()
            #retrieve all blog posts
            all_posts = BlogPostSerializer(posts, many=True).data
            response = {'results': all_posts}
            return Response(response)