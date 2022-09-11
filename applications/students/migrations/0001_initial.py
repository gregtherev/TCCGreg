# Generated by Django 4.1 on 2022-09-11 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90, verbose_name='Nome do aluno')),
                ('course', models.CharField(max_length=50, verbose_name='Curso')),
                ('joined_year', models.DateField(verbose_name='Ano de ingresso')),
            ],
            options={
                'verbose_name': 'Aluno',
                'verbose_name_plural': 'Alunos',
            },
        ),
    ]
