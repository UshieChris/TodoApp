from django.db import models

# Create your models here.
class Url(models.Model):
    title = models.CharField(max_length = 10000)
  