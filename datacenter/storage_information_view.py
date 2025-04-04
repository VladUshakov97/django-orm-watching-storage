import datetime

from django.shortcuts import render
from django.utils.timezone import localtime

from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.time_tracking import get_duration
from datacenter.time_tracking import format_duration


def storage_information_view(request):
    non_closed_visits = Visit.objects.filter(leaved_at=None)

    non_closed_visits_serialized = []
    for visit in non_closed_visits:
        duration = get_duration(visit)
        formatted_duration = format_duration(duration)

        non_closed_visits_serialized.append({
            'who_entered': visit.passcard.owner_name,
            'entered_at': localtime(visit.entered_at),
            'duration': formatted_duration,
        })

    context = {
        'non_closed_visits': non_closed_visits_serialized,
    }
    return render(request, 'storage_information.html', context)