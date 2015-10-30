# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import model_select_customized.models


class Migration(migrations.Migration):

    dependencies = [
        ('model_select_customized', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=model_select_customized.models.ForeignCustomDisplayKey(to='model_select_customized.Author', null=True),
        ),
    ]
