# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_id', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=100)),
                ('link', models.URLField()),
                ('price', models.IntegerField()),
                ('special', models.CharField(max_length=30)),
                ('notes', models.CharField(max_length=400)),
            ],
        ),
    ]
