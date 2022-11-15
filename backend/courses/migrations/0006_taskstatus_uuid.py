# Generated by Django 3.2.2 on 2022-11-13 11:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20221113_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskstatus',
            name='uuid',
            field=models.CharField(blank=True, default=uuid.uuid4, max_length=100, unique=True),
        ),
    ]