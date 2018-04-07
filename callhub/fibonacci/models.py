from django.db import models

# Create your models here.
class Store(models.Model):
    num = models.IntegerField(default=0)
    values = models.TextField()