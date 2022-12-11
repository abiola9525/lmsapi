from django.shortcuts import render

from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from itsdangerous import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import feed
from . serializers import feedSerializer

class FeedBack(APIView):
    
    def get(self, request):
        feed1 = feed.objects.all()
        serializer = feedSerializer(feed1, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = feedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response()

