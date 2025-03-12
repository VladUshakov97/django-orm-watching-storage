def get_duration(visit):
    if visit.leaved_at:
        return visit.leaved_at - visit.entered_at
    return timedelta()


def format_duration(duration):
    seconds = duration.total_seconds()
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    return f"{hours:02}:{minutes:02}"


def is_visit_long(visit, minutes=60):
    return get_duration(visit).total_seconds() > minutes * 60