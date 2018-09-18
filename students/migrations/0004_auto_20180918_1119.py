# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_student_student_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.ImageField(upload_to=b'img', verbose_name='\u0424\u043e\u0442\u043e', blank=True),
            preserve_default=True,
        ),
    ]
