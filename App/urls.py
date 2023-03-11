
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import *


router = DefaultRouter()
router.register(r'universityList', UniversityListViewSet, basename='university-Lists')
router.register(r'universityDetails', UniversityDetailsViewSet, basename='university-Details')

urlpatterns = [
    path('', include(router.urls))
]
