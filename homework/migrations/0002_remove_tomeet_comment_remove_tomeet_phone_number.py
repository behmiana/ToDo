# Generated by Django 4.1.1 on 2022-10-04 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tomeet',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='tomeet',
            name='phone_number',
        ),
    ]