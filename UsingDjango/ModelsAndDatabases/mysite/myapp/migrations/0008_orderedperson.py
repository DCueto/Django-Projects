# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20150320_0809'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderedPerson',
            fields=[
            ],
            options={
                'ordering': ['last_name'],
                'proxy': True,
            },
            bases=('myapp.personbase',),
        ),
    ]
