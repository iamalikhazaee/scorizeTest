from rest_framework import serializers
from .models import *

class countrySerializer(serializers.ModelSerializer):
     class Meta:
          model = Country
          fields = ["country"]

class citySerializer(serializers.ModelSerializer):
     country = countrySerializer()
     class Meta:
          model = City
          fields = ["city", "country"]

class UniversitySerializer(serializers.ModelSerializer):
     city = citySerializer()

     class Meta:
          model = University
          fields = ["id", "name", "city", "established_year"]
