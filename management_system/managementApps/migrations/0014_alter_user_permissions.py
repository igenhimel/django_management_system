# Generated by Django 4.2.4 on 2023-09-20 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managementApps', '0013_alter_user_permissions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='permissions',
            field=models.CharField(choices=[('read', 'Read'), ('write', 'Write')], default='read', max_length=255),
        ),
    ]
