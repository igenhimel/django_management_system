# Generated by Django 4.2.4 on 2023-09-20 09:58

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managementApps', '0004_alter_user_permissions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='permissions',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('Read', 'Read'), ('Write', 'Write')], max_length=20), default=list, size=None),
        ),
    ]
