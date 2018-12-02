# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from datetime import datetime

# Create your models here.

# Class Students
class Exam(models.Model):
    """Student Model"""

    class Meta(object):
        verbose_name = _(u"Exam")
        verbose_name_plural = _(u"Exam")

    date_and_time = models.DateTimeField(
        blank=False,
        verbose_name=_(u"Date and time of the event"))

    subject = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=_(u"Name subject"))

    teacher = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=_(u"Teacher"))

    notes = models.TextField(
        blank=True,
        verbose_name=_(u"Extra notes"))

    exam_group = models.ForeignKey('Group',
        verbose_name=_(u"Group"),
        blank=False,
        null=True,
        on_delete=models.PROTECT)

    def __unicode__(self):
        return u"%s" % (self.subject, )
