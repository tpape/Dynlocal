# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20150425_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='registration_history',
            field=models.TextField(blank=True, null=True),
        ),
    ]
