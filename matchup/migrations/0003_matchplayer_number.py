# Generated by Django 5.1.5 on 2025-02-07 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matchup', '0002_event_event_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchplayer',
            name='number',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
