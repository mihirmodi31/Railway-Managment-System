from django.db import models

# Create your models here.

class Feedback(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=25)
    feedbacks = models.TextField()