# Generated by Django 3.2.8 on 2021-10-07 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_song_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='dislikes',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
