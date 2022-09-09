from django.db import models
from django.contrib.auth.models import User


USER_TYPE = (
    (0, 'Admin'),
    (1, 'Team'),
    (2, 'Judge')
)

class Profile(User):
    name = models.CharField('Nome completo', max_length=255)
    user_type = models.PositiveIntegerField('Tipo de usuário', choices=USER_TYPE)

    def __str__(self):
        return self.name

