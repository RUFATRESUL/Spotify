# Generated by Django 5.0.1 on 2024-01-11 23:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('song', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='artist/images/')),
                ('updated', models.DateField(auto_now_add=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('updated', models.DateField(auto_now_add=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('followed_artists', models.ManyToManyField(related_name='followed_artists', to='user.artist')),
                ('liked_playlist', models.ManyToManyField(related_name='liked_playlists', to='song.playlist')),
                ('liked_songs', models.ManyToManyField(related_name='liked_songs', to='song.song')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
