# Generated by Django 3.2.6 on 2022-07-03 10:40

from django.conf import settings
from django.db import migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('job', '0011_auto_20220703_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='department_person',
            field=smart_selects.db_fields.ChainedManyToManyField(blank=True, chained_field='department', chained_model_field='username', horizontal=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
