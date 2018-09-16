# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse


# Views for Students
def students_list(request):
    students = (
        {'id': 1,
         'first_name': u'Подоба',
         'last_name': u'Віталій',
         'ticket': 235,
         'image': 'img/1.jpeg'},
        {'id': 2,
         'first_name': u'Корст',
         'last_name': u'Андрій',
         'ticket': 2123,
         'image': 'img/2.jpg'},
        {'id': 3,
         'first_name': u'Притула',
         'last_name': u'Тарас',
         'ticket': 5000,
         'image': 'img/3.jpg'},
    )

    groups = (
        {'id': 'МтМ-21',
         'monitor': 'Віталій Подоба'},
        {'id': 'МтМ-22',
         'monitor': 'Олег Корст'},
        {'id': 'Мтм-23',
         'monitor': 'Іван Іванов'},
    )
    return render(request, 'students/students_listing.html', {'students': students, 'groups': groups})

def students_add(request):
    return HttpResponse('<h1>Add Students</h1>')

def students_edit(request, sid):
    return HttpResponse('<h1>Edit Students %s </h1>' % sid)

def students_delete(request, sid):
    return HttpResponse('<h1>Delete students %s</h1>' % sid)