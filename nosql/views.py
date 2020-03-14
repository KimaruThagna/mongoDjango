from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
# Create your views here.



class AllResponses (APIView):
    def get(self, request):
        if request.method == 'GET':
            pass # get all responses in db