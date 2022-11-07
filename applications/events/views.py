from django.utils import timezone
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from applications.events.models import Event


@login_required
def events_running(request):
    """Just events that are running"""
    right_now = timezone.now()
    events = [event for event in Event.objects.filter(date=right_now.date())
              if event.is_active()]

    return render(request, 'events/events_running.html', {'events': events})
