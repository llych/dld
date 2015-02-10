# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('code_management', '0002_auto_20141230_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='codeproject',
            name='status',
            field=models.CharField(default='complete', max_length=20),
            preserve_default=False,
        ),
    ]
