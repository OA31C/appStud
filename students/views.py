# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

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
