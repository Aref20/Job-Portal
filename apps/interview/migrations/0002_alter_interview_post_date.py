# Generated by Django 3.2.6 on 2022-11-02 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interview',
            name='post_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاريخ ألإنشاء'),
        ),
    ]
