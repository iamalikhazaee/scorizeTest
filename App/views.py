from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework import pagination
from rest_framework.filters import SearchFilter
from .serializer import *
from .models import *



class ExamplePagination(pagination.PageNumberPagination):
       page_size = 10

class UniversityViewSet(viewsets.ModelViewSet):
    filter_backends = [SearchFilter]
    search_fields = ["name", "city__city", "city__country__country"]
    queryset = University.objects.all()
    serializer_class = UniversityListSerializer
    pagination_class = ExamplePagination