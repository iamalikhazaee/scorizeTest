from django.db import models

# Create your models here.

class Country(models.Model):
    country = models.CharField(max_length=225)

    def __str__(self):
        return self.country

class City(models.Model):
    city = models.CharField(max_length=225)
    country = models.ForeignKey(to=Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.city

class University(models.Model):
    city = models.ForeignKey(to=City, on_delete=models.CASCADE)
    name = models.CharField(max_length=225)
    acronym = models.CharField(max_length=10, null=True)
    logo = models.ImageField(upload_to=None, null=True)
    type = models.CharField(max_length=50, null=True)
    overview = models.TextField(blank=True)
    established_year = models.DateTimeField(null=False)
    total_std = models.CharField(max_length=225)
    international_std = models.CharField(max_length=225)
    website = models.CharField(max_length=225)
    apply_rate = models.CharField(max_length=10)

    def __str__(self):
        return self.name