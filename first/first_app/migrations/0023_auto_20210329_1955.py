# Generated by Django 3.1.5 on 2021-03-29 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0022_auto_20210329_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elim_lm_1_wyniki',
            name='result',
            field=models.CharField(blank=True, default='', max_length=600),
        ),
    ]
