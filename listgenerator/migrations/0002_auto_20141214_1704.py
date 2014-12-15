# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listgenerator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grocerylist',
            name='total_estimated',
            field=models.DecimalField(default=0, verbose_name=b'Estimated Total', max_digits=5, decimal_places=2, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='grocerylist',
            name='total_final',
            field=models.DecimalField(default=0, verbose_name=b'Final Total', max_digits=5, decimal_places=2, blank=True),
            preserve_default=True,
        ),
    ]
