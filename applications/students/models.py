from django.db import models


class Student(models.Model):
    name = models.CharField("Nome do aluno", max_length=90)
    course = models.CharField("Curso", max_length=50)
    joined_year = models.DateField("Ano de ingresso")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
