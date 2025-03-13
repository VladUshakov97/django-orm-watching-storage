import datetime

from django.shortcuts import render
from django.utils.timezone import localtime

from datacenter.models import Passcard
from datacenter.models import Visit

def active_passcards_view(request):
    active_passcards = Passcard.objects.filter(is_active=True)
    non_closed_visits = Visit.objects.filter(leaved_at=None)
    now = localtime()

    context = {
        'active_passcards': active_passcards,
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'active_passcards.html', context)