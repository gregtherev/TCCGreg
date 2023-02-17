"""This module contains the API for the accounts application."""
from ninja import Router

from .models import Team
from ..events.models import Question, Event
from .schemas import TeamSchema, AnswerSchema  # NoQA

router = Router()


@router.get("/hello")
def hello(request):
    return "Hello, World!"


@router.get("/leaderboard-teams/{event_id}")
def leaderboard_teams(request, event_id: int):
    teams = Team.objects.filter(event__id=event_id).order_by("-solved_questions", "-formated_time")
    event = Event.objects.get(id=event_id)
    teams_list = []

    print(event.id)

    for team in teams:
        team.formated_time = team.relative_time
        if team.penalties > 0:
            team.formated_time = team.formated_time + ((team.penalties) * event.punishment_value)
        team_info = TeamSchema(**team.__dict__)
        teams_list.append(team_info)

    return teams_list


@router.post("/submit-answer/{event_id}/{question_number}")
def submit_answer(request, answer_info: AnswerSchema, event_id: int,
                  question_number: int):
    team = Team.objects.get(pk=answer_info.team_id)
    question = Question.objects.get(event__id=event_id,
                                    qt_number=question_number)
    wr_qts = team.wr_questions.split(",")
    rc_qts = team.rc_questions.split(",")
    rt_qts = team.rt_questions.split(",")

    if str(question_number) in rc_qts or str(question_number) in rt_qts:
        return {"status": "ERROR", "reason": "question already solved"}

    if answer_info.answer.lower() != question.correct_ansnwer.lower():
        qt_set = wr_qts
        wr_set = set_add(qt_set, question_number)

        team.wr_questions = wr_set
        team.penalties += 1
        team.save()

        return {"status": "SUCCESS", "question_status": "wrong"}

    if answer_info.answer.lower() == question.correct_ansnwer.lower():
        team.solved_questions += 1
        team.relative_time += answer_info.time

        if str(question_number) in team.wr_questions:
            qt_set = wr_qts
            wr_set = set_remove(qt_set, question_number)
            qt_set = rc_qts
            rc_set = set_add(qt_set, question_number)

            team.wr_questions = wr_set
            team.rc_questions = rc_set
            team.save()

            return {"status": "SUCCESS", "question_status": "recovered"}

        qt_set = rt_qts
        rt_set = set_add(qt_set, question_number)

        team.rt_questions = rt_set
        team.save()

        return {"status": "SUCCESS", "question_status": "right"}


def set_add(qt_set: list, qt_id: int):
    _set = set(qt_set)
    _set.add(str(qt_id))

    if "" in _set:
        _set.remove("")

    return ",".join(_set)


def set_remove(qt_set: list, qt_id: int):
    _set = set(qt_set)
    _set.remove(str(qt_id))

    if "" in _set:
        _set.remove("")

    return ",".join(_set)

# TODO POPULAR O N-N SUBMISSAO A CADA SUBMISSAO ENVIADA PELO TIME
