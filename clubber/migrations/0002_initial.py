# Generated by Django 5.1.4 on 2024-12-09 15:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clubber', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='shirt',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clubber.team'),
        ),
        migrations.AddField(
            model_name='teamplayer',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clubber.player'),
        ),
        migrations.AddField(
            model_name='teamplayer',
            name='shirt',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='clubber.shirt'),
        ),
        migrations.AddField(
            model_name='teamplayer',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clubber.team'),
        ),
        migrations.AddField(
            model_name='team',
            name='players',
            field=models.ManyToManyField(through='clubber.TeamPlayer', to='clubber.player'),
        ),
    ]