from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def test_page_for_templates(request):
    return render(request, 'base_leaderboard.html')
