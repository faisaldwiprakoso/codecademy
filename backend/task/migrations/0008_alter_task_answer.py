# Generated by Django 3.2.2 on 2022-11-20 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0007_auto_20221119_0541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='answer',
            field=models.TextField(blank=True),
        ),
    ]
