# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listgenerator', '0002_auto_20141214_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grocerylist',
            name='total_estimated',
            field=models.DecimalField(default=0, verbose_name=b'Estimated Total', max_digits=5, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='grocerylist',
            name='total_final',
            field=models.DecimalField(default=0, verbose_name=b'Final Total', max_digits=5, decimal_places=2),
            preserve_default=True,
        ),
    ]
