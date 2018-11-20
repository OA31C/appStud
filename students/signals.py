# -*- coding: utf-8 -*-
import logging

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models.students import Student
from .models.groups import Group
from .models.exam import Exam


@receiver(post_save, sender=Student)
def log_student_updated_added_event(sender, **kwargs):
    """Writes information about newly added or updated student into log file"""
    logger = logging.getLogger(__name__)

    student = kwargs['instance']

    if kwargs['created']:
        logger.info("Student added: %s %s (ID: %d)", student.first_name, student.last_name, student.id)
    else:
        logger.info("Student updated: %s %s (ID: %d)", student.first_name, student.last_name, student.id)


@receiver(post_delete, sender=Student)
def log_student_deleted_event(sender, **kwargs):
    """Writes information about deleted student into log file"""
    logger = logging.getLogger(__name__)

    student = kwargs['instance']
    logger.info("Student deleted: %s %s (ID: %d)", student.first_name, student.last_name, student.id)


@receiver(post_save, sender=Group)
def log_group_update_added_event(sender, **kwargs):
    """Writes information about newly added or updated group into log file"""
    logger = logging.getLogger(__name__)

    group = kwargs['instance']
    if kwargs['created']:
        logger.info("Group added: %s leader: %s ", group.title, group.leader)
    else:
        logger.info("Group update: %s leader: %s", group.title, group.leader)


@receiver(post_delete, sender=Group)
def log_group_delete_event(sender, **kwargs):
    """Write information about deleted student into log file"""
    logger = logging.getLogger(__name__)

    group = kwargs['instance']
    logger.info('Group deleted: %s leader: %s ', group.title, group.leader)


@receiver(post_save, sender=Exam)
def log_exam_update_added_event(sender, **kwargs):
    """Writes information about newly added or update exam file"""

    logger = logging.getLogger(__name__)

    exam = kwargs['instance']
    if kwargs['created']:
        logger.info("Exam added: %s, date: (%s), group: %s ", exam.subject, exam.date_and_time, exam.exam_group)
    else:
        logger.info("Exam update: %s, date: (%s), group: %s ", exam.subject, exam.date_and_time, exam.exam_group)


@receiver(post_delete, sender=Group)
def log_exam_delete_event(sender, **kwargs):
    """Write information about deleted student into log file"""
    logger = logging.getLogger(__name__)

    exam = kwargs['instance']
    logger.info("Exam deleted: %s, date: (%s), group: %s ", exam.subject, exam.date_and_time, exam.exam_group)
