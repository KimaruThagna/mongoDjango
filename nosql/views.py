from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from .models import *
from .serializers import *
# Create your views here.
# statment = request.GET.get('statement')
class AllPosts (APIView):
    def get(self, request):
        if request.method == 'GET':
            #retrieve all blog possts
            all_posts = BlogPostSerializer(BlogPost.objects.all() ).data
            response = {'results': all_posts}
            return JsonResponse(response)