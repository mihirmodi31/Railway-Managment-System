from enum import unique
from django.db import models

# Create your models here.

class Trains(models.Model):
    name = models.CharField(max_length=25)
    pnr = models.IntegerField()
    source = models.CharField(max_length=15)
    destination = models.CharField(max_length=15)
    day = models.CharField(max_length=15)
    arrival = models.TimeField(auto_now=False, auto_now_add=False, blank=True)
    departure = models.TimeField(auto_now=False, auto_now_add=False, blank=True)