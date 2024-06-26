# Generated by Django 5.0.3 on 2024-03-29 15:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_rename_profile_attendee_eventorganizer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='eventDate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='eventNumberOfAttendees',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='eventOrganizer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.userprofile'),
        ),
    ]
