# -*- coding: utf-8 -*-
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from ..models.students import Student
from ..models.groups import Group
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Views for Students
def students_list(request):
    students = Student.objects.all()

    # try to order students list
    order_by = request.GET.get('order_by', '')
    if order_by in ('last_name', 'first_name', 'ticket'):
        students = students.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            students = students.reverse()

    paginator = Paginator(students, 3)
    page = request.GET.get('page')
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page
        students = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver
        # last page of results
        students = paginator.page(paginator.num_pages)


    groups = Group.objects.all()
    return render(request, 'students/students_listing.html', {'students': students, 'groups': groups})

def students_add(request):
    if request.method == "POST":
        # перевіряю яка кнопка натиснута
        # і обробляю відповідно запит
        if request.POST.get('add_button') is not None:

            # data for student object
            data = {
                'middle_name': request.POST.get('middle_name'),
                'notes': request.POST.get('notes')}
            # errors collection
            errors = {}

            # validate user input
            first_name = request.POST.get('first_name', '').strip()
            if not first_name:
                errors['first_name'] = u"Ім'я є обов'язковим"
            else:
                data['first_name'] = first_name

            last_name = request.POST.get('last_name', '').strip()
            if not last_name:
                errors['last_name'] = u"Прізвище є обов'язковим"
            else:
                data['last_name'] = last_name

            birthday = request.POST.get('birthday', '').strip()
            if not birthday:
                errors['birthday'] = u"Дата нородження є обов'язковою"
            else:
                try:
                    datetime.strptime(birthday, '%Y-%m-%d')
                except ValueError:
                    errors['birthday'] = u"Введіть коректний формат дати"
                else:
                    data['birthday'] = birthday
            ticket = request.POST.get('ticket', '').strip()
            if not ticket:
                errors['ticket'] = u"Номер об'єкта є обов'язковим"

            student_group = request.POST.get('student_group', '').strip()
            if not student_group:
                errors['student_group'] = u"Оберіть групу для студентів"
            else:
                groups = Group.objects.filter(pk=student_group)
                if len(groups) != 1:
                    errors['student_group'] = u"Оберіть коректну групу"
                else:
                    data['student_group'] = groups[0]
            photo = request.FILES.get('photo')
            if photo:
                data['photo'] = photo

            # TODO: add validation for all other fields

            # збергіаємо студента
            if not errors:
                student = Student(**data)

                student.save()
                return HttpResponseRedirect(reverse('home'))
            else:
                return render(request, 'students/students_add.html',
                              {'groups': Group.objects.all().order_by('title'),
                               'errors': errors})

        elif request.POST.get('cancel_button') is None:
            return HttpResponseRedirect(reverse('home'))
    else:
        return render(request, 'students/students_add.html',
                      {'groups': Group.objects.all().order_by('title')})

def students_edit(request, sid):
    return HttpResponse('<h1>Edit Students %s </h1>' % sid)

def students_delete(request, sid):
    return HttpResponse('<h1>Delete students %s</h1>' % sid)
