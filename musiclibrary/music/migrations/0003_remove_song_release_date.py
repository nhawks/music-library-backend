# Generated by Django 3.2.7 on 2021-10-01 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_alter_song_release_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='release_date',
        ),
    ]
