# Generated by Django 3.1.5 on 2021-03-21 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0008_auto_20210321_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='ekstraklasa',
            name='draws',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ekstraklasa',
            name='loses',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ekstraklasa',
            name='wins',
            field=models.IntegerField(default=0),
        ),
    ]