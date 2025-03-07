from datetime import timedelta

from django.shortcuts import render, get_object_or_404
from django.utils.timezone import localtime

from datacenter.models import Passcard
from datacenter.models import Visit

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


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    this_passcard_visits = Visit.objects.filter(passcard=passcard)

    this_passcard_visits_list = []
    for visit in this_passcard_visits:
        this_passcard_visits_list.append({
            'entered_at': localtime(visit.entered_at),
            'duration': format_duration(get_duration(visit)),
            'is_strange': is_visit_long(visit),
        })

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits_list,
    }
    return render(request, 'passcard_info.html', context)