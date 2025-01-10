# Create your views here.

from rest_framework.viewsets import ModelViewSet
# from rest_framework import generics

from .models import Category
from .serializers import CategorySerializer


# Create your views here.
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer