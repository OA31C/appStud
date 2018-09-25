# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime

# Create your models here.

# Class Students
class Exam(models.Model):
    """Student Model"""

    class Meta(object):
        verbose_name = u"Іспити"
        verbose_name_plural = u"Іспити"

    date_and_time = models.DateTimeField(
        blank=False,
        verbose_name=u"Дата і час проведення")

    subject = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Назва предмету")

    teacher = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Викладач")

    notes = models.TextField(
        blank=True,
        verbose_name=u"Додаткові нотатки")

    exam_group = models.ForeignKey('Group',
        verbose_name=u"Група",
        blank=False,
        null=True,
        on_delete=models.PROTECT)

    def __unicode__(self):
        return u"%s" % (self.subject, )
