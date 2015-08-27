# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=200)),
                ('publisher', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=2000)),
                ('genre', models.CharField(max_length=50)),
                ('pub_date', models.DateTimeField()),
                ('ISBN', models.CharField(max_length=20)),
                ('edition', models.CharField(max_length=30)),
            ],
        ),
    ]
