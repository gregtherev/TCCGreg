"""This module contains the API for the events application."""
from ninja import Router
from datetime import datetime

from ..events.models import Event, Submission
from utils.utils import calculate_remaining_time

router = Router()


@router.get("/hello")
def hello(request):
    return "Hello, World!"


@router.get("/{event_id}")
def event_info(request, event_id: int):
    event = Event.objects.get(pk=event_id)
    event_dict = {
        "event_name": event.name,
        "event_institution": event.institution.name,
        "event_total_questions": event.total_questions
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
    query = Submission.objects.filter(event_id=event_id).order_by("time")

    for item in query:
        submission = {
            "team": item.team.name,
            "question": item.question,
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
            "question": item.question,
            "answer": item.answer,
            "status": item.status,
            "sent_on": item.time,
        }
        submissions.append(submission)

    return submissions


@router.get("/right-submissions/{event_id}/{team_id}")
def right_submissions(request, event_id: int, team_id: int):
    right_questions = []
    query = Submission.objects.filter(event_id=event_id, team_id=team_id, status=1)

    for item in query:
        right_questions.append(item.question)

    return right_questions
