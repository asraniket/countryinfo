from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=200)
    capital = models.CharField(max_length=200)
    population = models.PositiveIntegerField()
    area = models.PositiveIntegerField()
