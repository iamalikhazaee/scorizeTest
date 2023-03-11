from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializer import *
from .models import *


class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversityListSerializer