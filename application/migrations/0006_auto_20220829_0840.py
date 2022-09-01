# Generated by Django 3.2.6 on 2022-08-29 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0005_alter_application_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='Car_License_Type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='application.license_type', verbose_name=' فئة الرخصة'),
        ),
        migrations.AlterField(
            model_name='application',
            name='Warranty',
            field=models.CharField(blank=True, choices=[('Yes', 'نعم'), ('No', 'لا')], default='No', max_length=3, null=True, verbose_name=' هل يمكنك إحضار كفالة عدلية '),
        ),
        migrations.AlterField(
            model_name='application_form',
            name='Car_License_Type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='application.license_type', verbose_name=' فئة الرخصة'),
        ),
    ]
