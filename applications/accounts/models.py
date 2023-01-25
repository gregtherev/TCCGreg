from django.db import models
from django.contrib.auth.models import User
from ..students.models import Student


class Team(User):
    name = models.CharField('Nome da equipe', max_length=255)
    solved_questions = models.IntegerField("Questões resolvidas",
                                           default=0,
                                           blank=True)
    relative_time = models.PositiveIntegerField("Tempo relativo", default=0)
    penalties = models.PositiveIntegerField(
        "Quantidade de penalidades", default=0)
    formated_time = models.PositiveIntegerField(
        "Tempo relativo + penalidades", null=True)
    rt_questions = models.CharField('Questões acertadas', max_length=255,
                                    default="")
    wr_questions = models.CharField('Questões erradas', max_length=255,
                                    default="")
    rc_questions = models.CharField('Questões recuperadas', max_length=255,
                                    default="")
    # TODO adicionar atributo para subir o logo da equipe
    event = models.ForeignKey('events.Event', on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Equipe'

        verbose_name_plural = 'Equipes'


class Judge(User):
    name = models.CharField('Nome completo', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Juíz'
        verbose_name_plural = 'Juízes'
