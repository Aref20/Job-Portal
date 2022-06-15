# Generated by Django 2.1.7 on 2022-06-15 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='Application_Have_Car',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='N', max_length=3),
        ),
        migrations.AddField(
            model_name='application',
            name='Application_Socility_Status',
            field=models.CharField(choices=[('Married', 'Married'), ('Single', 'Single')], default='Single', max_length=10),
        ),
        migrations.AlterField(
            model_name='application',
            name='Application_Car_License',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='N', max_length=3),
        ),
        migrations.AlterField(
            model_name='application',
            name='Application_NID',
            field=models.CharField(max_length=10, verbose_name='الرقم الوطني'),
        ),
    ]
