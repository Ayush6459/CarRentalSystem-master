# Generated by Django 2.0.2 on 2018-03-10 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='middle_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='phone_no',
        ),
    ]
