from django.db import models

# Create your models here.

class Price(models.Model):
    price = models.FloatField(null=True, blank=True, default=None)
    time = models.DateTimeField(default=None)