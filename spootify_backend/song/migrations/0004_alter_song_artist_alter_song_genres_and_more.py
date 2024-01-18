# Generated by Django 5.0.1 on 2024-01-16 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0003_alter_song_playlists'),
        ('user', '0006_alter_customer_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='artist',
            field=models.ManyToManyField(related_name='songs', to='user.artist'),
        ),
        migrations.AlterField(
            model_name='song',
            name='genres',
            field=models.ManyToManyField(related_name='songs', to='song.genre'),
        ),
        migrations.AlterField(
            model_name='song',
            name='playlists',
            field=models.ManyToManyField(blank=True, null=True, related_name='songs', to='song.playlist'),
        ),
    ]
