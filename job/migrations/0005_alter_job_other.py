# Generated by Django 3.2.6 on 2022-08-30 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_alter_job_expiration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='other',
            field=models.TextField(blank=True, max_length=3000, verbose_name=' مهارات أخرى '),
        ),
    ]
