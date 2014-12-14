# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20141214_1618'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroceryList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.SlugField(unique=True)),
                ('name', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('total_estimated', models.DecimalField(verbose_name=b'Estimated Total', max_digits=5, decimal_places=2)),
                ('total_final', models.DecimalField(verbose_name=b'Final Total', max_digits=5, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ListProducts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.PositiveSmallIntegerField(default=1)),
                ('grocerylist', models.ForeignKey(to='listgenerator.GroceryList')),
                ('product', models.ForeignKey(to='products.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='grocerylist',
            name='products',
            field=models.ManyToManyField(to='products.Product', through='listgenerator.ListProducts'),
            preserve_default=True,
        ),
    ]
