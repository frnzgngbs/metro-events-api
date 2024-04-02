# Generated by Django 5.0.3 on 2024-04-02 08:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_nonorganizerevent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nonorganizerevent',
            name='user_profile',
        ),
        migrations.AlterField(
            model_name='nonorganizerevent',
            name='eventOrganizer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.userprofile'),
        ),
    ]
