"""This module contains the API for the accounts application."""
from ninja import Router

from .models import Team
from .schemas import TeamSchema  # NoQA

router = Router()


@router.get("/hello")
def hello(request):
    return "Hello, World!"


@router.get("/leaderboard-teams/{event_id}")
def leaderboard_teams(request, event_id: int):
    teams = Team.objects.filter(event__id=event_id)
    event = Team.event
    teams_list = []

    for team in teams:
        team.formated_time = ((team.penalties*60) * event.punishment_value
                              if team.penalties else team.relative_time)
        team_info = TeamSchema(**team.__dict__)
        teams_list.append(team_info)

    return teams_list
