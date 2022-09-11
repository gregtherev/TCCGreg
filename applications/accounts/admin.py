from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple

from .models import Team, Judge
from ..students.models import Student
from .forms import JudgeCreationForm, TeamCreationForm


class TeamForm(TeamCreationForm):
    class Meta:
        model = Team
        fields = ["username", "name", "students"]

    students = forms.ModelMultipleChoiceField(
        label='Alunos',
        queryset=Student.objects.all(),
        required=False,
        widget=FilteredSelectMultiple(('Alunos'), True))


class JudgeForm(JudgeCreationForm):
    class Meta:
        model = Judge
        fields = ["username", "name"]


class TeamAdmin(admin.ModelAdmin):
    form = TeamForm


class JudgeAdmin(admin.ModelAdmin):
    form = JudgeForm


admin.site.register(Team, TeamAdmin)
admin.site.register(Judge, JudgeAdmin)
