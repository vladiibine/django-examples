# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_complex_filter', '0002_auto_20151030_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='available',
            field=models.BooleanField(default=False),
        ),
    ]
