from datetime import timedelta

from django.shortcuts import render, get_object_or_404
from django.utils.timezone import localtime

from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.time_tracking import get_duration
from datacenter.time_tracking import format_duration
from datacenter.time_tracking import is_visit_long


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    this_passcard_visits = Visit.objects.filter(passcard=passcard)

    this_passcard_visits_serialized = []
    for visit in this_passcard_visits:
        this_passcard_visits_serialized.append({
            'entered_at': localtime(visit.entered_at),
            'duration': format_duration(get_duration(visit)),
            'is_strange': is_visit_long(visit),
        })

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits_serialized,
    }
    return render(request, 'passcard_info.html', context)