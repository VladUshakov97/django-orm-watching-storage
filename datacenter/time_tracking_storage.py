from django.utils.timezone import localtime

SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60
DEFAULT_VISIT_MINUTES = 60

def get_duration(visit):
    now = localtime()
    return now - visit.entered_at


def format_duration(duration):
    seconds = duration.total_seconds()
    hours = int(seconds // SECONDS_IN_HOUR)
    minutes = int((seconds % SECONDS_IN_HOUR) // SECONDS_IN_MINUTE)
    return f"{hours:02}:{minutes:02}"