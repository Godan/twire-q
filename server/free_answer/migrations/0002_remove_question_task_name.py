# Generated by Django 3.2.7 on 2021-09-24 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('free_answer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='task_name',
        ),
    ]
