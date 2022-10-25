"""This module contains the API for the accounts application."""
from ninja import Router

from .models import Team
from .schemas import TeamInfo  # NoQA

router = Router()


@router.get("/hello")
def hello(request):
    return "Hello, World!"


@router.get("/leaderboard-teams/{event_id}")
def leaderboard_teams(request, event_id: int):
    teams = Team.objects.filter(event__id=event_id)
    event = Team.event
    teams_list = []
    team_dict = {}

    for team in teams:
        formated_time = (team.penalties * 60) * event.punishment_value

        team_dict["name"] = team.name
        team_dict["solved_questions"] = team.solved_questions
        team_dict["relative_time"] = team.relative_time
        team_dict["penalties"] = team.penalties
        team_dict["rt_questions"] = team.rt_questions
        team_dict["wr_questions"] = team.wr_questions
        team_dict["rc_questions"] = team.rc_questions
        team_dict["formated_time"] = team.relative_time + formated_time

        teams_list.append(team_dict)

    teams_list = {teams_list}

    return teams_list
