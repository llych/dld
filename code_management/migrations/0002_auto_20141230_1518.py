# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('code_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='codeproject',
            name='svn_password',
            field=models.CharField(default='admin', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='codeproject',
            name='svn_user',
            field=models.CharField(default='admin', max_length=100),
            preserve_default=False,
        ),
    ]
