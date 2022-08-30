from django.db import models

class Events(models.Model):
    name = models.CharField(max_length=255, null=False)
    date = models.DateField(null=False)
    type = models.TextChoices('Envio automático', 'Validação de juíz')
    punishment_value = models.IntegerField(\
        verbose_name='Valor em minutos de cada punição acumulada',
        default=20)


class Questions(models.Model):
    question_text = models.CharField()
    image_path = models.CharField(null=False)
    correct_ansnwer = models.CharField(max_length=1, null=False)


class Institutions(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=50)


class Submissions(models.Model):
    question = models.CharField()
    asnwer = models.CharField()
    time = models.TimeField()
    status = models.TextChoices('Correto', 'Incorreto')
    #event, team foreign keys



