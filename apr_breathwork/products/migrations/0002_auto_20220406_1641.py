# Generated by Django 3.2 on 2022-04-06 16:41

import datetime
from django.db import migrations, models
import time


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productvariant',
            name='attendance_limit',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='productvariant',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='productvariant',
            name='meeting_invite_link',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='productvariant',
            name='places_sold',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]