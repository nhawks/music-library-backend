# Generated by Django 3.2.7 on 2021-10-01 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_auto_20211001_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='likes',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
