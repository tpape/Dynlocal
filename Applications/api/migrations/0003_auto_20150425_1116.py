# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20150421_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='registration_history',
            field=models.TextField(blank=True),
        ),
    ]
