# Generated by Django 5.0.1 on 2024-01-13 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='playlists',
            field=models.ManyToManyField(blank=True, null=True, to='song.playlist'),
        ),
    ]
