from rest_framework import serializers
from .models import *

class UniversitySerializer(serializers.ModelSerializer):
     class Meta:
          model = University
          fields = ["id", "name", "city", "established_year", "total_std", "international_std", "apply_rate"]
