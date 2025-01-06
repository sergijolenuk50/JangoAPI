from django.shortcuts import render

# Create your views here.
from .models import Category
from .serializers import CategorySerializer
from rest_framework import generics

# Create your views here.
class CategoryViewSet(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer