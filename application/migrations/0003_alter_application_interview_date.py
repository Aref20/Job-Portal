# Generated by Django 3.2.6 on 2022-07-04 15:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_application_job_app'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='Interview_Date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
