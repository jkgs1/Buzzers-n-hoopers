# Generated by Django 5.1.6 on 2025-02-24 12:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matchup', '0007_alter_match_starttime'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='clockPaused',
            field=models.BooleanField(default=True, editable=False),
        ),
        migrations.AddField(
            model_name='match',
            name='timePaused',
            field=models.DateTimeField(default=datetime.datetime(2025, 2, 24, 12, 30, 39, 866710, tzinfo=datetime.timezone.utc), editable=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='event_type',
            field=models.CharField(choices=[('1P', '1 Point'), ('2P', '2 Points'), ('3P', '3 Points'), ('FP', 'Personal foul'), ('FO', 'Other foul'), ('EX', 'Exchange'), ('TO', 'Timeout'), ('MS', 'Match start'), ('CP', 'Clock pause'), ('CR', 'Clock resume')], max_length=2),
        ),
    ]
