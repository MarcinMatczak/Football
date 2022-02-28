# Generated by Django 3.1.5 on 2021-03-29 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0024_elim_lm_1_last_scored'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Elim_ECL_1_wyniki',
        ),
        migrations.DeleteModel(
            name='Elim_ECL_2_wyniki',
        ),
        migrations.DeleteModel(
            name='Elim_ECL_3_wyniki',
        ),
        migrations.DeleteModel(
            name='Elim_ECL_4_wyniki',
        ),
        migrations.DeleteModel(
            name='Elim_LE_3_wyniki',
        ),
        migrations.DeleteModel(
            name='Elim_LE_4_wyniki',
        ),
        migrations.DeleteModel(
            name='Elim_LM_1_wyniki',
        ),
        migrations.DeleteModel(
            name='Elim_LM_2_wyniki',
        ),
        migrations.DeleteModel(
            name='Elim_LM_3_wyniki',
        ),
        migrations.DeleteModel(
            name='Elim_LM_4_wyniki',
        ),
        migrations.AddField(
            model_name='elim_ecl_1',
            name='last_scored',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
        migrations.AddField(
            model_name='elim_ecl_2',
            name='last_scored',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
        migrations.AddField(
            model_name='elim_ecl_3',
            name='last_scored',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
        migrations.AddField(
            model_name='elim_ecl_4',
            name='last_scored',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
        migrations.AddField(
            model_name='elim_le_3',
            name='last_scored',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
        migrations.AddField(
            model_name='elim_le_4',
            name='last_scored',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
        migrations.AddField(
            model_name='elim_lm_2',
            name='last_scored',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
        migrations.AddField(
            model_name='elim_lm_3',
            name='last_scored',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
        migrations.AddField(
            model_name='elim_lm_4',
            name='last_scored',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
    ]