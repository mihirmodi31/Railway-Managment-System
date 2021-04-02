from django.db import models

# Create your models here.
class Tickets(models.Model):
    train_id = models.IntegerField
    date = models.DateField()
    no = models.IntegerField()
    total_price = models.IntegerField()
    passangers = models.CharField(max_length=1000)
    ages = models.CharField(max_length=500)
