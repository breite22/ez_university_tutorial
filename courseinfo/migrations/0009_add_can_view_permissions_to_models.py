# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-27 18:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courseinfo', '0008_group_data'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='calendarperiod',
            options={'ordering': ['calendar_period_id'], 'permissions': (('view_calendarperiod', 'Can view calendar period'),)},
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['course_number'], 'permissions': (('view_course', 'Can view course'),)},
        ),
        migrations.AlterModelOptions(
            name='instructor',
            options={'ordering': ['last_name', 'first_name'], 'permissions': (('view_instructor', 'Can view instructor'),)},
        ),
        migrations.AlterModelOptions(
            name='section',
            options={'ordering': ['course__course_number', 'section_name', 'semester'], 'permissions': (('view_section', 'Can view section'),)},
        ),
        migrations.AlterModelOptions(
            name='semester',
            options={'ordering': ['year', 'calendar_period__calendar_period_id'], 'permissions': (('view_semester', 'Can view semester'),)},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['last_name', 'first_name'], 'permissions': (('view_student', 'Can view student'),)},
        ),
        migrations.AlterField(
            model_name='semester',
            name='calendar_period',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='semesters', to='courseinfo.CalendarPeriod'),
        ),
    ]
