import datetime

from django.shortcuts import render
from django.utils.timezone import localtime

from datacenter.models import Passcard
from datacenter.models import Visit

def get_duration(visit):
    now = localtime()
    return now - visit.entered_at


def format_duration(duration):
    seconds = duration.total_seconds()
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    return f"{hours:02}:{minutes:02}"


def storage_information_view(request):
    non_closed_visits = Visit.objects.filter(leaved_at=None)

    non_closed_visits_list = []
    for visit in non_closed_visits:
        duration = get_duration(visit)
        formatted_duration = format_duration(duration)

        non_closed_visits_list.append({
            'who_entered': visit.passcard.owner_name,
            'entered_at': localtime(visit.entered_at),
            'duration': formatted_duration,
        })

    context = {
        'non_closed_visits': non_closed_visits_list,
    }
    return render(request, 'storage_information.html', context)