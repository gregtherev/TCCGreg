# Generated by Django 4.1 on 2023-01-24 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_team_relative_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='penalties',
            field=models.PositiveIntegerField(default=0, verbose_name='Quantidade de penalidades'),
        ),
    ]
