# Generated by Django 4.1.1 on 2022-10-04 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0003_alter_tomeet_date_of_meeting'),
    ]

    operations = [
        migrations.AddField(
            model_name='tomeet',
            name='phone_number',
            field=models.IntegerField(default=0),
        ),
    ]
