from django.db import models


class Ranking(models.Model):
    # team, event foreign keys
    solved_questions = models.IntegerField()
    relative_time = models.TimeField()

