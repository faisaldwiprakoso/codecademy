# Generated by Django 3.2.2 on 2022-11-21 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0009_alter_task_default_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='error_message',
            field=models.TextField(blank=True),
        ),
    ]
