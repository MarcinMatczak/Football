# Generated by Django 3.1.5 on 2021-03-20 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_liga'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Liga',
            new_name='Liga16',
        ),
        migrations.RenameField(
            model_name='liga16',
            old_name='teams',
            new_name='team1',
        ),
    ]
