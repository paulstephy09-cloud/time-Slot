from django.shortcuts import render
from .models import TimeSlot


def timetable_view(request):
    slots = TimeSlot.objects.all()

    context = {
        'slots': slots,
    }

    return render(request, 'timetable.html', context)