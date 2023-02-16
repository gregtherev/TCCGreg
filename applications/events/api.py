"""This module contains the API for the events application."""
from ninja import Router
from datetime import timedelta, datetime, date

from ..events.models import Event

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
