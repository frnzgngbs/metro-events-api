# Generated by Django 5.0.3 on 2024-03-29 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_event_eventdate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='eventNumberOfAttendees',
            field=models.IntegerField(default=0),
        ),
    ]
