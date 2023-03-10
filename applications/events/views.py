from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from applications.events.models import Event


def events_running(request):
    """Just events that are running"""
    # right_now = timezone.now()
    if not request.user.is_anonymous and not request.user.is_superuser:
        return redirect('event_details')
    event_list = []
    events = Event.objects.all()
    for event in events:
        if event.is_active:
            event_list.append(event)

    return render(request, 'events/events_running.html', {'events': events})


@login_required
def event_details(request):
    """Details of the registered user"""
    return render(request, 'events/event_details.html')


def event_details_spec(request, event: id):
    """Details of specific event for spectators"""
    if not request.user.is_anonymous and not request.user.is_superuser:
        return redirect('event_details')
    event = Event.objects.get(id=event)
    return render(request, 'events/event_details.html', {'event': event})
