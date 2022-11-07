from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from applications.events.models import Event


@login_required
def leaderboard(request, event: int):
    event = Event.objects.get_or_404(id=event)
    return render(request, 'leaderboard/leaderboard.html', {'event': event})
