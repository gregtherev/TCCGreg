from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def leaderboard(request, event: int):
    return render(request, 'leaderboard/leaderboard.html', {'event': event})
