# Generated by Django 4.1.1 on 2022-09-20 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('context', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='Additional_File',
        ),
    ]
