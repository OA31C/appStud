# -*- coding: utf-8 -*-
from datetime import datetime
from django.shortcuts import render
from django.http import  HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms import ModelForm
from django.views.generic import UpdateView, DeleteView
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions
from ..models.exam import Exam
from ..models.groups import Group


def exam_list(request):
    exams = Exam.objects.all()
    return render(request, 'exam/exam_list.html', {'exams': exams})

def exam_add(request):
    if request.method == "POST":
        # перевіряю яка кнопка натиснута
        # і обробляю відповідно запит
        if request.POST.get('add_button') is not None:

            # data for student object
            data = {
                'notes': request.POST.get('notes')}
            # errors collection
            errors = {}

            # validate user input
            date_and_time = request.POST.get('date_and_time', '').strip()
            if not date_and_time:
                errors['date_and_time'] = u"Дата і час є обов'язковою"
            else:
                try:
                    datetime.strptime(date_and_time, '%Y-%m-%d %X') #1983-10-10 21:30:00
                except Exception:
                    errors['date_and_time'] = u"Введіть коректний формат дати та часу"
                else:
                    data['date_and_time'] = date_and_time

            subject = request.POST.get('subject', '').strip()
            if not subject:
                errors['subject'] = u"Предмет є обов'язковим"
            else:
                data['subject'] = subject

            teacher = request.POST.get('teacher', '').strip()
            if not teacher:
                errors['teacher'] = u"Викладач є обов'язковим"
            else:
                data['teacher'] = teacher

            exam_group = request.POST.get('exam_group', '').strip()
            if not exam_group:
                errors['exam_group'] = u"Оберіть групу для іспитів"
            else:
                groups = Group.objects.filter(pk=exam_group)
                if len(groups) != 1:
                    errors['exam_group'] = u"Оберіть коректну групу"
                else:
                    data['exam_group'] = groups[0]
            # TODO: add validation for all other fields

            # збергіаємо студента
            if not errors:
                exam = Exam(**data)

                exam.save()
                return HttpResponseRedirect(reverse('exam'))
            else:
                return render(request, 'exam/exam_add.html',
                              {'groups': Group.objects.all().order_by('title'),
                               'errors': errors})

        elif request.POST.get('cancel_button') is not None:
            return HttpResponseRedirect(reverse('exam'))
    else:
        return render(request, 'exam/exam_add.html',
                      {'groups': Group.objects.all().order_by('title')})


class ExamUpdateForm(ModelForm):
    class Meta:
        model = Exam

    def __init__(self, *args, **kwargs):
        super(ExamUpdateForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)

        # set form tag attributes
        self.helper.form_action = reverse('edit_exam',
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

class ExamUpdateView(UpdateView):
    model = Exam
    template_name = 'exam/exam_edit.html'
    form_class = ExamUpdateForm

    # success_url = '/'
    @property
    def success_url(self):
        return u"%s?status_message=Іспит успішно збережено!" % reverse('exam')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(u"%s?status_message=Редагування іспита відмінено!" % reverse('exam'))
        else:
            return super(ExamUpdateView, self).post(request, *args, **kwargs)

class ExamDeleteView(DeleteView):
    model = Exam
    template_name = 'exam/exam_confirm_delete.html'

    @property
    def success_url(self):
        return u"%s?status_message=Іспит успішно видалено!" % reverse('exam')
