# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listgenerator', '0003_auto_20141214_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='listproducts',
            name='total',
            field=models.DecimalField(default=0, verbose_name=b'Final Total', max_digits=5, decimal_places=2),
            preserve_default=True,
        ),
    ]
