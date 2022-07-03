# Generated by Django 3.2.6 on 2022-07-03 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('job', '0008_remove_job_department_person'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='department',
        ),
        migrations.AddField(
            model_name='title',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='groub', to='auth.group'),
        ),
    ]
