# Generated by Django 3.2.2 on 2022-11-19 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solution', '0006_alter_solution_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='answer',
            field=models.TextField(blank=True),
        ),
    ]
