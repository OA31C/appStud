from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# Students List
def students_list(request):
    return render(request, 'students/students_listing.html', {})

def students_add(request):
    return HttpResponse('<h1>Add Students</h1>')

def students_edit(request):
    return HttpResponse('<h1>Edit Students</h1>')

def students_delete(request):
    return HttpResponse('<h1>Delete students</h1>')

# Groups
def groups_list(request):
    return render(request, 'students/groups_listing.html', {})

def groups_add(request):
    return HttpResponse('<h1>Groups Add</h1>')

def groups_edit(request):
    return HttpResponse('<h1>Groups Edit</h1>')

def groups_delete(request):
    return HttpResponse('<h1>Groups Delete</h1>')

# Journal
def journal_list(request):
    return render(request, 'students/journal_listing.html', {})

def journal_student(request):
    return HttpResponse('<h1>Journal student</h1>')

def journal_update(request):
    return HttpResponse('<h1>Journal update</h1>')
