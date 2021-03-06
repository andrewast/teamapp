# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-28 09:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('due_date', models.DateTimeField()),
                ('comment', models.TextField()),
                ('priority', models.IntegerField(choices=[(0, 'Low'), (1, 'Normal'), (2, 'Medium'), (3, 'High')], default=1)),
                ('status', models.IntegerField(choices=[(0, 'Started'), (1, 'In-progress'), (2, 'Stopped'), (3, 'Completed')], default=1)),
                ('assigners', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('status', '-created'),
            },
        ),
    ]
