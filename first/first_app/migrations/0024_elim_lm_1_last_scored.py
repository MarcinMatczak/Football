# Generated by Django 3.1.5 on 2021-03-29 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0023_auto_20210329_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='elim_lm_1',
            name='last_scored',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
    ]
