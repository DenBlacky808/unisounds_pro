# Generated by Django 3.2.9 on 2021-11-16 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='track',
            name='short_desc',
        ),
    ]