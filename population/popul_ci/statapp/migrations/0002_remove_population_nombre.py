# Generated by Django 2.2.6 on 2019-10-31 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('statapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='population',
            name='nombre',
        ),
    ]
