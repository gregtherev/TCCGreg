from django.db import models

class Institutions(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
