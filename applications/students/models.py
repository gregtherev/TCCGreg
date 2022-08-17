from django.db import models

class ModelName(models.Model):
    name = models.CharField(max_length=90)
    course = models.CharField(max_length=50)
    joined_year = models.DateField()