# Generated by Django 4.0.1 on 2022-02-26 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0004_redditmessage_redditmessagesender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reddit',
            name='message',
        ),
        migrations.RemoveField(
            model_name='reddit',
            name='pause',
        ),
    ]
