# Generated by Django 3.2.6 on 2022-06-28 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0007_auto_20220628_1145'),
    ]

    operations = [
        migrations.AddField(
            model_name='computer_skill',
            name='Computer_Skill_Application',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Computer_Skill', to='application.application'),
        ),
        migrations.AddField(
            model_name='previous_company',
            name='Previous_Company_Application',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Previous_Company', to='application.application'),
        ),
        migrations.AddField(
            model_name='previous_coworker',
            name='Previous_Coworker_Application',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Previous_Coworker', to='application.application'),
        ),
        migrations.AddField(
            model_name='training',
            name='Training_Application',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Training', to='application.application'),
        ),
    ]
