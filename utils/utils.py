from datetime import timedelta, datetime

from applications.events.models import Event


def calculate_remaining_time(event: Event):
    remaining_time = (event.start_time + timedelta(minutes=event.duration))
    remaining_time = remaining_time.replace(tzinfo=None)
    now = datetime.utcnow()
    remaining_seconds = (remaining_time-now).total_seconds()

    return remaining_seconds
