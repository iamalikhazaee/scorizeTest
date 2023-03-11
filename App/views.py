from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from .serializer import *
from .models import *

from rest_framework import pagination

class ExamplePagination(pagination.PageNumberPagination):
       page_size = 10

class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversityListSerializer
    pagination_class = ExamplePagination