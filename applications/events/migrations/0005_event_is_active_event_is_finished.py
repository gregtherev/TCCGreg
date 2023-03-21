# Generated by Django 4.1 on 2023-03-06 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_event_final_results_event_partial_results'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='is_finished',
            field=models.BooleanField(default=False),
        ),
    ]
