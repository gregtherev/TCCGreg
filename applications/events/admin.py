from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple

from .models import Institution, Event, Question
from ..accounts.models import Judge


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = "__all__"

    judges = forms.ModelMultipleChoiceField(
        label='Juízes',
        queryset=Judge.objects.all(),
        required=False,
        widget=FilteredSelectMultiple(('Juízes'), True))


class EventAdmin(admin.ModelAdmin):
    form = EventForm


admin.site.register(Institution)
admin.site.register(Event, EventAdmin)
admin.site.register(Question)
