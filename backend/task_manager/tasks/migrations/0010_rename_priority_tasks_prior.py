# Generated by Django 5.1.1 on 2025-02-21 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0009_rename_task_id_comments_task_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tasks',
            old_name='priority',
            new_name='prior',
        ),
    ]
