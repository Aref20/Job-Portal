# Generated by Django 3.2.6 on 2022-07-27 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0005_alter_language_language_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='HR_Interview_Approval',
            field=models.BooleanField(default=False, verbose_name=' موافقة الموارد البشرية لتاريخ المقابلة '),
        ),
    ]
