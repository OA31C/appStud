# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import  HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from ..models.exam import Exam


def exam_list(request):
    exams = Exam.objects.all()
    return render(request, "students/exam_list.html", {'exams': exams})