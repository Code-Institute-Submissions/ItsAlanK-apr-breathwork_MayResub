# Generated by Django 3.2 on 2022-04-06 16:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20220406_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='productvariant',
            name='time',
            field=models.TimeField(default=datetime.time(13, 0)),
        ),
    ]