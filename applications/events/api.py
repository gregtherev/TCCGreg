"""This module contains the API for the events application."""
from ninja import Router
from datetime import timedelta, datetime, date

from ..events.models import Event, Question

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
    event = Event.objects.get(pk=event_id)
    remaining_time = (datetime.combine(date.today(), event.start_time)
                      + timedelta(hours=event.duration))
    now = datetime.now()
    remaining_seconds = (remaining_time-now).total_seconds()

    event_dict = {
        "date": event.date.strftime("%d/%m/%Y"),
        "remaining_seconds": int(remaining_seconds)
    }

    return event_dict
