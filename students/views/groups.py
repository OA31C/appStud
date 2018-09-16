# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse


# Groups
def groups_list(request):
    groups = (
        {'id': 'МтМ-21',
         'monitor': 'Віталій Подоба'},
        {'id': 'МтМ-22',
         'monitor': 'Олег Корст'},
        {'id': 'Мтм-23',
         'monitor': 'Іван Іванов'},
    )
    return render(request, 'students/groups_listing.html', {'groups': groups})

def groups_add(request):
    return HttpResponse('<h1>Groups Add</h1>')

def groups_edit(request, sid):
    return HttpResponse('<h1>Groups Edit</h1 %s>' % sid)

def groups_delete(request, sid):
    return HttpResponse('<h1>Groups Delete</h1> %sid </h1>' % sid)