# Generated by Django 3.1.7 on 2021-09-06 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Taskapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.TextField(max_length=200, null=True),
        ),
    ]
