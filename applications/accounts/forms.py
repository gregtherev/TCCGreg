from django.contrib.auth.forms import UserCreationForm

from .models import Judge, Team


class TeamCreationForm(UserCreationForm):
    class Meta:
        model = Team
        fields = "__all__"


class JudgeCreationForm(UserCreationForm):
    class Meta:
        model = Judge
        fields = "__all__"
