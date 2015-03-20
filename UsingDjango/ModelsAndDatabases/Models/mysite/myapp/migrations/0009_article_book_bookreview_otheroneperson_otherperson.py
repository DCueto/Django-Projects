# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_orderedperson'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('article_id', models.AutoField(serialize=False, primary_key=True)),
                ('headline', models.CharField(max_length=50)),
                ('body', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BookReview',
            fields=[
                ('article_ptr', models.OneToOneField(parent_link=True, auto_created=True, to='myapp.Article')),
                ('book_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='myapp.Book')),
            ],
            options={
            },
            bases=('myapp.book', 'myapp.article'),
        ),
        migrations.CreateModel(
            name='OtherOnePerson',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('myapp.person', models.Model),
        ),
        migrations.CreateModel(
            name='OtherPerson',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('myapp.person',),
        ),
    ]
