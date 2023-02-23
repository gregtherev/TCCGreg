from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple

from .models import Institution, Event, Question, Submission
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
    list_display = ('name', 'institution', 'date')
    search_fields = ['name', 'institution__name', 'date']


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('qt_number', 'event')
    search_fields = ['qt_number', 'event__name']


class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('team', 'event', 'question', 'answer', 'time', 'status')
    search_fields = ['team__name', 'event__name']


admin.site.register(Institution)
admin.site.register(Event, EventAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Submission, SubmissionAdmin)
