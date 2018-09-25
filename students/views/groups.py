# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from ..models.groups import Group
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
    return render(request, 'students/groups_listing.html', {'groups': groups})

def groups_add(request):
    return HttpResponse('<h1>Groups Add</h1>')

def groups_edit(request, sid):
    return HttpResponse('<h1>Groups Edit %s </h1>' % sid)

def groups_delete(request, sid):
    return HttpResponse('<h1>Groups Delete %sid</h1>' % sid)
