# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0003_auto_20150425_2357'),
    ]

    operations = [
        migrations.AddField(
            model_name='join',
            name='ip_address',
            field=models.CharField(default=b'null', max_length=120),
        ),
        migrations.AddField(
            model_name='join',
            name='ref_id',
            field=models.CharField(default=b'null', max_length=120),
        ),
    ]
