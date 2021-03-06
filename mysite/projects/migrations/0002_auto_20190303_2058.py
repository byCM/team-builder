# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2019-03-04 05:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('p', 'Pending'), ('a', 'Accepted'), ('r', 'Rejected')], default='p', max_length=1)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to=settings.AUTH_USER_MODEL)),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Position')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='skills',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('android', 'Android Developer'), ('designer', 'Designer'), ('java', 'Java Developer'), ('php', 'PHP Developer'), ('python', 'Python Developer'), ('rails', 'Rails Developer'), ('wordpress', 'Wordpress Devloper'), ('ios', 'iOS Developer')], default='', max_length=52),
            preserve_default=False,
        ),
    ]
