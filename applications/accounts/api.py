"""This module contains the API for the accounts application."""
from datetime import datetime
from ninja import Router

from .application import list_leaderboard
from ..events.models import Question, Event, Submission
from .models import Team
from .schemas import AnswerSchema  # NoQA
from utils.utils import calculate_remaining_time

router = Router()


@router.get("/hello")
def hello(request):
    return "Hello, World!"


@router.get("/leaderboard-teams/{event_id}")
def leaderboard_teams(request, event_id: int):
    event = Event.objects.get(id=event_id)
    if not event.is_active and event.is_finished:
        return event.final_results

    return event.partial_results


@router.get("/final-leaderboard/{event_id}")
def final_leaderboard(request, event_id: int):
    event = Event.objects.get(id=event_id)

    return event.final_results


@router.post("/submit-answer/{event_id}/{question_number}")
def submit_answer(request, answer_info: AnswerSchema, event_id: int,
                  question_number: int):
    team = Team.objects.get(pk=answer_info.team_id)
    question = Question.objects.get(event__id=event_id,
                                    qt_number=question_number)
    event = Event.objects.get(pk=event_id)
    wr_qts = team.wr_questions.split(",")
    rc_qts = team.rc_questions.split(",")
    rt_qts = team.rt_questions.split(",")
    now = datetime.utcnow()

    if len(answer_info.answer) > 1:
        return {"status": "ERROR", "reason": "Answer len must be 1 char"}

    if str(question_number) in rc_qts or str(question_number) in rt_qts:
        return {"status": "ERROR", "reason": "question already solved"}

    submission = Submission(
                        question=question,
                        answer=answer_info.answer,
                        time=now,
                        status=1,
                        event=team.event,
                        team=team
                        )

    if answer_info.answer.lower() != question.correct_ansnwer.lower():
        qt_set = wr_qts
        wr_set = set_add(qt_set, question_number)

        team.wr_questions = wr_set
        team.penalties += 1
        team.save()
        submission.status = 0
        submission.save()

        message = {"status": "SUCCESS", "question_status": "wrong"}

    elif answer_info.answer.lower() == question.correct_ansnwer.lower():
        start_time = question.event.start_time.replace(tzinfo=None)
        diff = now - start_time
        team.solved_questions += 1
        team.relative_time += (diff).total_seconds()

        if str(question_number) in team.wr_questions:
            qt_set = wr_qts
            wr_set = set_remove(qt_set, question_number)
            qt_set = rc_qts
            rc_set = set_add(qt_set, question_number)

            team.wr_questions = wr_set
            team.rc_questions = rc_set
            team.save()
            submission.save()

            message = {"status": "SUCCESS", "question_status": "recovered"}

        else:
            qt_set = rt_qts
            rt_set = set_add(qt_set, question_number)

            team.rt_questions = rt_set
            team.save()
            submission.save()

            message = {"status": "SUCCESS", "question_status": "right"}

    remaining_seconds = calculate_remaining_time(event)
    leaderboard = list_leaderboard(event)
    if remaining_seconds > 360:
        event.partial_results = leaderboard
    event.final_results = leaderboard
    event.save()

    return message


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
