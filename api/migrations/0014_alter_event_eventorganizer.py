# Generated by Django 5.0.3 on 2024-03-30 13:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_joinrequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='eventOrganizer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.userprofile'),
        ),
    ]
