from unicodedata import name
from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=255, null=False)
    date = models.DateField(null=False)
    type = models.TextChoices('Envio automático', 'Validação de juíz')
    punishment_value = models.IntegerField(\
        verbose_name='Valor em minutos de cada punição acumulada',
        default=20)

    def __str__(self):
        return self.name


class Question(models.Model):
    question = models.TextField('Questão')
    # image = models.ImageField('Upload de imagem', upload_to=None, height_field=None, width_field=None, max_length=None)
    correct_ansnwer = models.CharField(max_length=1, null=False)

    def __str__(self):
        return f'Questão {self.id}'


class Institution(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=50)

    def __str__(self):
        return name


class Submission(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=2)
    time = models.TimeField()
    status = models.TextChoices('Correto', 'Incorreto')
    #event, team foreign keys
    # event = models.ForeignKey(OTHERMODEL, on_delete=models.CASCADE)