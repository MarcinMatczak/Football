# Generated by Django 3.1.5 on 2021-03-20 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0005_auto_20210320_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ekstraklasa',
            name='image',
            field=models.ImageField(upload_to='upload/'),
        ),
    ]