# Generated by Django 3.2.6 on 2022-08-31 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_job_career_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='expiration_date',
            field=models.DateField(verbose_name='تاريخ إنتهاء الوظيفة '),
        ),
    ]
