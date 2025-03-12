from django.utils.timezone import localtime

def get_duration(visit):
    now = localtime()
    return now - visit.entered_at


def format_duration(duration):
    seconds = duration.total_seconds()
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    return f"{hours:02}:{minutes:02}"