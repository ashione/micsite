# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('nodeip', models.CharField(max_length=20)),
                ('nodename', models.CharField(max_length=20)),
                ('nodeinfo', models.CharField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserRecords',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('starttime', models.DateTimeField()),
                ('endtime', models.DateTimeField()),
                ('lemo', models.CharField(max_length=500)),
                ('userid', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
