# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-27 21:03
from __future__ import unicode_literals

from django.db import migrations, models

CALENDAR_PERIODS = [
    {
        "calendar_period_id": 10,
        "calendar_period_name": "Spring",
    },
    {
        "calendar_period_id": 20,
        "calendar_period_name": "Summer",
    },
    {
        "calendar_period_id": 30,
        "calendar_period_name": "Fall",
    },
    {
        "calendar_period_id": 9999,
        "calendar_period_name": "TemporaryValue",
    },
]


def add_calendar_period_data(apps, schema_editor):
    CalendarPeriod = apps.get_model('courseinfo', 'CalendarPeriod')
    for calendar_period in CALENDAR_PERIODS:
        calendar_period_object = CalendarPeriod.objects.create(
            calendar_period_id=calendar_period['calendar_period_id'],
            calendar_period_name=calendar_period['calendar_period_name']
        )


def remove_calendar_period_data(apps, schema_editor):
    CalendarPeriod = apps.get_model('courseinfo', 'CalendarPeriod')
    for calendar_period in CALENDAR_PERIODS:
        calendar_period_object = CalendarPeriod.objects.get(
            calendar_period_id=calendar_period['calendar_period_id']
        )
        calendar_period_object.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('courseinfo', '0003_semester_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='CalendarPeriod',
            fields=[
                ('calendar_period_id', models.IntegerField(primary_key=True, serialize=False)),
                ('calendar_period_name', models.CharField(max_length=45, unique=True)),
            ],
            options={
                'ordering': ['calendar_period_id'],
            },
        ),
        migrations.RunPython(
            add_calendar_period_data,
            remove_calendar_period_data
        )
    ]