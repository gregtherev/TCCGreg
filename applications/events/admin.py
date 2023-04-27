from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple

from .models import Institution, Event, Submission
from ..accounts.models import Judge


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ('partial_results', 'final_results', )

    judges = forms.ModelMultipleChoiceField(
        label='Juízes',
        queryset=Judge.objects.all(),
        required=True,
        widget=FilteredSelectMultiple(('Juízes'), True))


class EventAdmin(admin.ModelAdmin):
    form = EventForm
    list_display = ('name', 'institution', 'date')
    search_fields = ['name', 'institution__name', 'date']


class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('team', 'event', 'question', 'answer', 'time', 'status')
    search_fields = ['team__name', 'event__name']


admin.site.register(Institution)
admin.site.register(Event, EventAdmin)
admin.site.register(Submission, SubmissionAdmin)
