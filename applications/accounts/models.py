from django.db import models

class Teams(models.Model):
    name = models.CharField(max_length=100)
    relative_time = models.TimeField()
    solved_questions = models.IntegerField()
    image_path = models.CharField()


class Judges(models.Model):
    name = models.CharField()


class Admin(models.Model):
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)