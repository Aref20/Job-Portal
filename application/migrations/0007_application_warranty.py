# Generated by Django 3.2.6 on 2022-07-31 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0006_alter_application_hr_interview_approval'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='Warranty',
            field=models.CharField(choices=[('Yes', 'نعم'), ('No', 'لا')], default='No', max_length=3, verbose_name=' هل يمكنك إحضار كفالة عدلية '),
        ),
    ]
