# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_category_is_food'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='is_food',
            field=models.BooleanField(default=False, verbose_name=b'Is This Food?'),
            preserve_default=True,
        ),
    ]
