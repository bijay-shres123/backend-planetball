# Generated by Django 4.0.3 on 2022-03-23 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0003_profilefeeditem'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_coach',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_player',
            field=models.BooleanField(default=False),
        ),
    ]