# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_place_restaurant'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonBase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('place_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='myapp.Place')),
                ('customers', models.ManyToManyField(related_name='provider', to='myapp.Place')),
            ],
            options={
            },
            bases=('myapp.place',),
        ),
        migrations.CreateModel(
            name='MyPerson',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('myapp.personbase',),
        ),
        migrations.AlterModelOptions(
            name='place',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='restaurant',
            options={'ordering': ['serves_pizza', 'serves_hot_dogs']},
        ),
    ]
