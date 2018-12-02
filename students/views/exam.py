# -*- coding: utf-8 -*-
from datetime import datetime
from django.shortcuts import render
from django.http import  HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms import ModelForm
from django.views.generic import UpdateView, DeleteView
from django.utils.translation import ugettext as _


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
                errors['date_and_time'] = _(u"Date and time are required")
            else:
                try:
                    datetime.strptime(date_and_time, '%Y-%m-%d %X') #1983-10-10 21:30:00
                except Exception:
                    errors['date_and_time'] = _(u"Enter the correct date and time format")
                else:
                    data['date_and_time'] = date_and_time

            subject = request.POST.get('subject', '').strip()
            if not subject:
                errors['subject'] = _(u"Subject is required")
            else:
                data['subject'] = subject

            teacher = request.POST.get('teacher', '').strip()
            if not teacher:
                errors['teacher'] = _(u"Teacher is required")
            else:
                data['teacher'] = teacher

            exam_group = request.POST.get('exam_group', '').strip()
            if not exam_group:
                errors['exam_group'] = _(u"Select the group for the exam")
            else:
                groups = Group.objects.filter(pk=exam_group)
                if len(groups) != 1:
                    errors['exam_group'] = _(u"Select the correct group")
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
            Submit('add_button', _(u"Save"), css_class="btn btn-primary"),
            Submit('cancel_button', _(u"Cancel"), css_class="btn btn-link"),
        )


class ExamUpdateView(UpdateView):
    model = Exam
    template_name = 'exam/exam_edit.html'

    # success_url = '/'
    @property
    def success_url(self):
        return u"%s?status_message=%s" % (reverse('exam'), _(u"Exam updated successfully!"))

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(u"%s?status_message=%s" % (reverse('exam'), _(u"Student update canceled!")))
        else:
            return super(ExamUpdateView, self).post(request, *args, **kwargs)


class ExamDeleteView(DeleteView):
    model = Exam
    template_name = 'exam/exam_confirm_delete.html'

    @property
    def success_url(self):
        return u"%s?status_message=%s" % (reverse('exam'), _(u"Student deleted successfully!"))
