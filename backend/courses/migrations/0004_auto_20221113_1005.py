# Generated by Django 3.2.2 on 2022-11-13 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20221113_0857'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_file_extension',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(blank=True, to='courses.Course'),
        ),
        migrations.AlterField(
            model_name='student',
            name='tasks',
            field=models.ManyToManyField(blank=True, to='courses.Task'),
        ),
    ]