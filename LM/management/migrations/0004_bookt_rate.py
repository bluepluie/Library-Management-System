# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_auto_20151106_2342'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookt',
            name='rate',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
