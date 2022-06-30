# Generated by Django 3.2.6 on 2022-06-30 13:31

from django.db import migrations, models
import django.db.models.deletion
import job.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Nature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nature_name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField(max_length=3000)),
                ('post_date', models.DateField(auto_now_add=True)),
                ('vacancy', models.IntegerField(blank=True)),
                ('salary', models.IntegerField(blank=True)),
                ('experience_min', models.IntegerField(blank=True)),
                ('experience_max', models.IntegerField(blank=True)),
                ('status', models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE')], default=job.models.Status['ACTIVE'], max_length=255)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.group')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='job.location')),
                ('nature', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='job.nature')),
            ],
        ),
    ]
