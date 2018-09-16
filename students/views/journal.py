# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

# Journal
def journal_list(request):
    groups = (
        {'id': 'МтМ-21',
         'monitor': 'Віталій Подоба'},
        {'id': 'МтМ-22',
         'monitor': 'Олег Корст'},
        {'id': 'Мтм-23',
         'monitor': 'Іван Іванов'},
    )
    return render(request, 'students/journal_listing.html', {'groups': groups})

def journal_student(request, sid):
    return HttpResponse('<h1>Journal student %s </h1>' % sid)

def journal_update(request):
    return HttpResponse('<h1>Journal update</h1>')