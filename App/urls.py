
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import *


router = DefaultRouter()
router.register(r'universityList', UniversityListViewSet, basename='university-Lists')

urlpatterns = [
    path('', include(router.urls))
]
