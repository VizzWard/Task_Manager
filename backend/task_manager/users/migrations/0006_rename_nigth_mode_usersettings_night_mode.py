# Generated by Django 5.1.1 on 2025-02-20 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_rename_user_id_usersettings_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usersettings',
            old_name='nigth_mode',
            new_name='night_mode',
        ),
    ]
