# -*- coding: utf-8 -*-
from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms import ModelForm
from django.views.generic import UpdateView, DeleteView

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions

from ..models import Student, Group

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
            else:
                data['ticket'] = ticket

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

        elif request.POST.get('cancel_button') is not None:
            return HttpResponseRedirect(reverse('home'))
    else:
        return render(request, 'students/students_add.html',
                      {'groups': Group.objects.all().order_by('title')})

class StudentUpdateForm(ModelForm):
    class Meta:
        model = Student

    def __init__(self, *args, **kwargs):
        super(StudentUpdateForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)

        # set form tag attributes
        self.helper.form_action = reverse('students_edit',
                                          kwargs={'pk': kwargs['instance'].id})
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'

        # set form field properties
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'

        # add buttons
        self.helper.layout[-1] = FormActions(
            Submit('add_button', u'Зберегти', css_class="btn btn-primary"),
            Submit('cancel_button', u'Скасувати', css_class="btn btn-link"),
        )


class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'students/students_edit.html'
    form_class = StudentUpdateForm

    # success_url = '/'
    @property
    def success_url(self):
        return u"%s?status_message=Студента успішно збережено!" % reverse('home')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(u"%s?status_message=Редагування студента відмінено!" % reverse('home'))
        else:
            return super(StudentUpdateView, self).post(request, *args, **kwargs)



class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/students_confirm_delete.html'
    # form_class = StudentUpdateForm

    # success_url = '/'
    @property
    def success_url(self):
        return u"%s?status_message=Студента успішно видалено!" % reverse('home')
