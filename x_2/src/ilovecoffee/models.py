from django.db import models

# Create your models here.
class coffee(models.Model):
    name = models.TextField()
    bean_from = models.TextField()
    price = models.FloatField()