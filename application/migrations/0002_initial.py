# Generated by Django 3.2.6 on 2022-08-02 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('application', '0001_initial'),
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='language_form',
            name='Language_Name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='job.language', verbose_name='اللغة '),
        ),
        migrations.AddField(
            model_name='language',
            name='Language_Application',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Language', to='application.application', verbose_name=' اللغات'),
        ),
        migrations.AddField(
            model_name='language',
            name='Language_Name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='job.language', verbose_name='اللغة '),
        ),
        migrations.AddField(
            model_name='computer_skill_form',
            name='Computer_Skill_Application',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Computer_Skill', to='application.application_form', verbose_name=' برامج الحاسوب'),
        ),
        migrations.AddField(
            model_name='computer_skill',
            name='Computer_Skill_Application',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Computer_Skill', to='application.application', verbose_name=' برامج الحاسوب'),
        ),
        migrations.AddField(
            model_name='application_form',
            name='Car_License_Type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='application.license_type', verbose_name=' فئة الرخصة'),
        ),
        migrations.AddField(
            model_name='application',
            name='Car_License_Type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='application.license_type', verbose_name=' فئة الرخصة'),
        ),
        migrations.AddField(
            model_name='application',
            name='Job_App',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='JA', to='job.job', verbose_name=' الوظيفة'),
        ),
    ]
