# Generated by Django 3.1.4 on 2021-04-05 11:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('discreption', models.TextField(blank=True)),
                ('task_st_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('task_end_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('is_important', models.BooleanField(default=False)),
                ('is_published', models.BooleanField(default=True)),
                ('is_Finished', models.BooleanField(default=False)),
            ],
        ),
    ]
