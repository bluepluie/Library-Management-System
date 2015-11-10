# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_auto_20151106_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowinfo',
            name='ReturnDate',
            field=models.DateField(null=True, blank=True),
        ),
    ]
