from ..events.models import Event
from .models import Team
from .schemas import TeamSchema  # NoQA


def list_leaderboard(event: Event):
    teams = Team.objects.filter(event__id=event.id)\
        .order_by("-solved_questions", "-formated_time")

    teams_dict = {}
    teams_list = []
    for team in teams:
        team.formated_time = team.relative_time

        if team.penalties > 0:
            team.formated_time = team.formated_time + ((team.penalties) * (event.punishment_value * 60))

        team_info = TeamSchema(**team.__dict__)
        teams_list.append(team_info.__dict__)

    teams_dict['teams'] = teams_list

    return teams_dict
