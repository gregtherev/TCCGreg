"""This module contains the API for the events application."""
from ninja import Router
from datetime import datetime

from ..events.models import Event, Question, Submission
from utils.utils import calculate_remaining_time

router = Router()


@router.get("/hello")
def hello(request):
    return "Hello, World!"


@router.get("/{event_id}")
def event_info(request, event_id: int):
    event = Event.objects.get(pk=event_id)
    total_questions = Question.objects.filter(event__id=event.id).count()
    event_dict = {
        "event_name": event.name,
        "event_institution": event.institution.name,
        "event_total_questions": total_questions
    }

    return event_dict


@router.get("/event_duration/{event_id}")
def event_duration(request, event_id: int):
    started = False
    event = Event.objects.get(pk=event_id)
    if event.start_time.replace(tzinfo=None) < datetime.utcnow():
        started = True
    remaining_seconds = calculate_remaining_time(event)
    event_dict = {
        "date": event.date.strftime("%d/%m/%Y"),
        "remaining_seconds": int(remaining_seconds),
        "started": started
    }

    return event_dict


@router.get("/submissions/{event_id}")
def all_team_submissions(request, event_id: int):
    if not request.user.is_superuser:
        return

    submissions = []
    query = Submission.objects.filter(event_id=event_id)

    for item in query:
        submission = {
            "team": item.team.name,
            "question": item.question.qt_number,
            "answer": item.answer,
            "status": item.status,
            "sent_on": item.time
        }
        submissions.append(submission)

    return submissions


@router.get("/submissions/{event_id}/{team_id}")
def team_submissions(request, event_id: int, team_id: int):
    submissions = []
    query = Submission.objects.filter(event_id=event_id, team_id=team_id)

    for item in query:
        submission = {
            "question": item.question.qt_number,
            "answer": item.answer,
            "status": item.status,
            "sent_on": item.time,
        }
        submissions.append(submission)

    return submissions
