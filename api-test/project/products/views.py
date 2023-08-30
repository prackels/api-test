from django.shortcuts import render
from .serializers import iphoneserializer
from .models import iphone
from rest_framework import viewsets

class iphone_api(viewsets.ModelViewSet):
    queryset = iphone.objects.all()
    serializer_class = iphoneserializer