# Generated by Django 4.1.1 on 2022-10-04 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0002_remove_tomeet_comment_remove_tomeet_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tomeet',
            name='date_of_meeting',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]