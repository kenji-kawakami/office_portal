# Generated by Django 3.0.8 on 2020-08-21 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('office_info', '0008_auto_20200816_2334'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff',
            old_name='staff',
            new_name='departmental',
        ),
    ]
