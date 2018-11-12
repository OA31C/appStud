# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from ..models.groups import Group
from ..models.students import Student
from django.forms import ModelForm
from django.views.generic import UpdateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions

# Groups


def groups_list(request):
    groups = Group.objects.all()

    # try to order students list
    order_by = request.GET.get('order_by', '')
    if order_by in ('title', 'leader'):
        groups = groups.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            groups = groups.reverse()

    # Paginator
    paginator = Paginator(groups, 3)

    page = request.GET.get('page')
    try:
        groups = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        groups = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        groups = paginator.page(paginator.num_pages)
    return render(request, 'group/groups_listing.html', {'groups': groups})


def groups_add(request):

    if request.method == 'POST':

        if request.POST.get('add_button') is not None:
            data = {}
            errors = {}

            title = request.POST.get('title', '').strip()
            if not title:
                errors['title'] = u"Назва гурпи є обов'язкова"
            else:
                data['title'] = title

            notes = request.POST.get('notes', '').strip()
            if notes:
                data['notes'] = notes

            if not errors:
                group = Group(**data)

                group.save()
            return HttpResponseRedirect(reverse('groups'))
        elif request.POST.get('cancel_button') is not None:
            return HttpResponseRedirect(reverse('groups'))
    else:
        return render(request, 'group/groups_add.html', {'students': Student.objects.all()})


class GroupUpdateForm(ModelForm):
    class Meta:
        model = Group

    def __init__(self, *args, **kwargs):
        super(GroupUpdateForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)

        # set form tag attributes
        self.helper.form_action = reverse('edit_groups',
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


class GroupUpdateView(UpdateView):
    model = Group
    template_name = 'group/groups_edit.html'
    form_class = GroupUpdateForm

    # success_url = '/'
    @property
    def success_url(self):
        return u"%s?status_message=Групу успішно збережено!" % reverse('groups')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(u"%s?status_message=Редагування групи відмінено!" % reverse('groups'))
        else:
            return super(GroupUpdateView, self).post(request, *args, **kwargs)


class GroupDeleteView(DeleteView):
    model = Group
    template_name = 'group/groups_confirm_delete.html'

    @property
    def success_url(self):
        return u"%s?status_message=Групу успішно видалено!" % reverse('groups')

