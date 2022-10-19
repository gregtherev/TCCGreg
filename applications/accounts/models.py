from django.db import models
from django.contrib.auth.models import User
from ..students.models import Student


class Team(User):
    name = models.CharField('Nome da equipe', max_length=255)
    solved_questions = models.IntegerField("Questões resolvidas",
                                           default=0,
                                           blank=True)
    relative_time = models.TimeField("Tempo relativo", null=True, blank=True)
    penalties = models.IntegerField(
        "Quantidade de penalidades", null=True, blank=True)
    rt_questions = models.CharField('Questões acertadas', null=True, 
                                    max_length=255)
    wr_questions = models.CharField('Questões erradas', null=True,
                                    max_length=255)
    rc_questions = models.CharField('Questões recuperadas', null=True,
                                    max_length=255)
    # TODO adicionar atributo para subir o logo da equipe
    # event = models.ForeignKey('applications.events', on_delete=models.CASCADE) ## NOQA ## RESOLVER O IMPORT CIRCULAR DESSA MERDA
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
