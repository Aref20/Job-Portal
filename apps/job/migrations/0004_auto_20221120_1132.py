# Generated by Django 3.2.6 on 2022-11-20 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_auto_20221120_0915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobhistory',
            name='close_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name=' تاريخ إغلاق الوظيفة'),
        ),
        migrations.AlterField(
            model_name='jobhistory',
            name='open_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name=' تاريخ فتح الوظيفة'),
        ),
    ]
