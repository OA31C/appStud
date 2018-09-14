from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# Students List
def students_list(request):
    return render(request, 'students/students_listing.html', {})

def students_add(request):
    return HttpResponse('<h1>Add Students</h1>')

def students_edit(request, sid):
    return HttpResponse('<h1>Edit Students %s </h1>' % sid)

def students_delete(request, sid):
    return HttpResponse('<h1>Delete students %s</h1>' % sid)

# Groups
def groups_list(request):
    return render(request, 'students/groups_listing.html', {})

def groups_add(request):
    return HttpResponse('<h1>Groups Add</h1>')

def groups_edit(request, sid):
    return HttpResponse('<h1>Groups Edit</h1 %s>' % sid)

def groups_delete(request, sid):
    return HttpResponse('<h1>Groups Delete</h1> %sid </h1>' % sid)

# Journal
def journal_list(request):
    return render(request, 'students/journal_listing.html', {})

def journal_student(request, sid):
    return HttpResponse('<h1>Journal student %s </h1>' % sid)

def journal_update(request):
    return HttpResponse('<h1>Journal update</h1>')
