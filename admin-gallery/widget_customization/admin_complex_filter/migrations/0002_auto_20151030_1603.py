# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_complex_filter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_id',
            field=models.CharField(max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='link',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='notes',
            field=models.CharField(max_length=400, blank=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='special',
            field=models.CharField(max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='title',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
