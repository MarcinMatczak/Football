# Generated by Django 3.1.5 on 2021-03-29 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0021_auto_20210329_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elim_ecl_1_wyniki',
            name='result',
            field=models.CharField(blank=True, max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='elim_ecl_2_wyniki',
            name='result',
            field=models.CharField(blank=True, max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='elim_ecl_3_wyniki',
            name='result',
            field=models.CharField(blank=True, max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='elim_ecl_4_wyniki',
            name='result',
            field=models.CharField(blank=True, max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='elim_le_3_wyniki',
            name='result',
            field=models.CharField(blank=True, max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='elim_le_4_wyniki',
            name='result',
            field=models.CharField(blank=True, max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='elim_lm_2_wyniki',
            name='result',
            field=models.CharField(blank=True, max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='elim_lm_3_wyniki',
            name='result',
            field=models.CharField(blank=True, max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='elim_lm_4_wyniki',
            name='result',
            field=models.CharField(blank=True, max_length=600, null=True),
        ),
    ]