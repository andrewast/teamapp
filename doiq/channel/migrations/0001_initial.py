# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-02 21:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import django.utils.timezone
import doiq.channel.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChannelMembership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Join date')),
                ('counter_unread', models.PositiveIntegerField(default=0, verbose_name='Total unread messages')),
                ('private_channel_opened', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='channelmembership',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=255, verbose_name='Channel Name')),
                ('channel_uid', models.CharField(db_index=True, default=doiq.channel.models.get_channel_uid, max_length=255, unique=True, verbose_name='Unique channel identifier')),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'Private-relate'), (2, 'Channel-relate')], default=2, verbose_name='Type of channel')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Description')),
                ('opened', models.BooleanField(default=True, verbose_name='Opened')),
                ('members_contacts', models.TextField(blank=True, null=True)),
                ('members', models.ManyToManyField(blank=True, related_name='channels', through='channel.ChannelMembership', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),

    ]
