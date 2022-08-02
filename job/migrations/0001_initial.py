# Generated by Django 3.2.6 on 2022-08-02 13:51

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Career_Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=300, verbose_name='  مستوى الخبرة')),
            ],
            options={
                'verbose_name': 'مستوى الخبرة ',
                'verbose_name_plural': ' مستوى الخبرة ',
            },
        ),
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='الدرجة العلمية')),
            ],
            options={
                'verbose_name': ' الدرجة العلمية',
                'verbose_name_plural': ' الدرجة العلمية ',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name=' اللغة')),
            ],
            options={
                'verbose_name': 'اللغات  ',
                'verbose_name_plural': ' اللغات ',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=300, verbose_name=' الموقع')),
            ],
            options={
                'verbose_name': ' الموقع ',
                'verbose_name_plural': ' الموقع ',
            },
        ),
        migrations.CreateModel(
            name='Nature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nature_name', models.CharField(max_length=300, verbose_name=' طبيعة العمل')),
            ],
            options={
                'verbose_name': ' طبيعة العمل ',
                'verbose_name_plural': ' طبيعة العمل ',
            },
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name=' عنوان الوظيفة')),
                ('description', models.TextField(max_length=3000, verbose_name='الوصف ')),
                ('warranty', models.BooleanField(blank=True, default=False, verbose_name='  هل يتطلب إحضار كفالة عدلية ')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.group', verbose_name=' القسم')),
                ('department_person', smart_selects.db_fields.ChainedManyToManyField(blank=True, chained_field='department', chained_model_field='groups', horizontal=True, null=True, related_name='usertitle', to=settings.AUTH_USER_MODEL, verbose_name='department_person')),
            ],
            options={
                'verbose_name': ' عنوان الوظيفة ',
                'verbose_name_plural': ' عنوان الوظيفة ',
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_date', models.DateField(auto_now_add=True, verbose_name=' تاريخ الانشاء')),
                ('vacancy', models.IntegerField(blank=True, verbose_name='الشواغر ')),
                ('salary', models.IntegerField(blank=True, null=True, verbose_name='الراتب ')),
                ('experience_min', models.IntegerField(blank=True, verbose_name='الخبرة من')),
                ('experience_max', models.IntegerField(blank=True, verbose_name='الخبرة الى ')),
                ('status', models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE')], default='INACTIVE', max_length=255, verbose_name='حالة الوظيفة ')),
                ('expiration_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='تاريخ إنتهاء الوظيفة ')),
                ('required_competencies', models.TextField(max_length=3000, verbose_name='المهارات المطلوبة ')),
                ('other', models.TextField(max_length=3000, verbose_name=' مهارات أخرى ')),
                ('Education', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='job.degree', verbose_name='الدرجة العلمية ')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.group', verbose_name=' القسم')),
                ('langs', models.ManyToManyField(null=True, to='job.Language', verbose_name='اللغات ')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='job.location', verbose_name='الموقع ')),
                ('nature', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='job.nature', verbose_name='طبيعة العمل ')),
                ('title', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='job.title', verbose_name='عنوان الوظيفة ')),
            ],
            options={
                'verbose_name': ' الوظائف ',
                'verbose_name_plural': ' الوظائف ',
            },
        ),
    ]
