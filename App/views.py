from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework import pagination
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .serializer import *
from .models import *



class ExamplePagination(pagination.PageNumberPagination):
       page_size = 10

class UniversityListViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ["name", "city__city", "city__country__country"]
    filterset_fields = ['city__city', 'city__country__country']
    queryset = University.objects.all()
    serializer_class = UniversityListSerializer
    pagination_class = ExamplePagination