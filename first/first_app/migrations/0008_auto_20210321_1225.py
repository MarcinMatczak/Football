# Generated by Django 3.1.5 on 2021-03-21 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0007_auto_20210321_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ekstraklasa',
            name='strength',
            field=models.IntegerField(default=2000),
        ),
    ]
