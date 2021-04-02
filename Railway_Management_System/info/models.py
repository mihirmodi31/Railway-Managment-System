from django.db import models

# Create your models here.
class Tickets(models.Model):
    date = models.DateField()
    no = models.IntegerField()
    total_price = models.IntegerField()
    passangers = models.CharField(max_length=1000)
    ages = models.CharField(max_length=500)

class Avail(models.Model):
    pnr = models.CharField(max_length=15)
    seat = models.IntegerField()
