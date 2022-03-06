from django.db import models


class Location(models.Model):
    address = models.CharField(max_length=30)
    addresstype = models.CharField(max_length=20)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    latitude = models.FloatField()
    longitude = models.FloatField()