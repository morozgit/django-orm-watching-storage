from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.all()[0]
    visits = Visit.objects.all()
    this_passcard_visits = []
    permit = get_object_or_404(Passcard, passcode=passcode)
    one_person_visit = visits.filter(passcard=permit)
    for one_visit in one_person_visit:
        passcard_visit = {
            'entered_at': one_visit.entered_at,
            'duration': one_visit.format_duration(one_visit.get_duration(one_visit)),
            'is_strange': one_visit.is_visit_long(one_visit, minutes=15)
        }
        this_passcard_visits.append(passcard_visit)
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
