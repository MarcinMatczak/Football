# Generated by Django 3.1.5 on 2021-03-30 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0025_auto_20210329_2229'),
    ]

    operations = [
        migrations.CreateModel(
            name='ECL_group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264)),
                ('points', models.IntegerField(default=0)),
                ('scored', models.IntegerField(default=0)),
                ('conceded', models.IntegerField(default=0)),
                ('wins', models.IntegerField(default=0)),
                ('loses', models.IntegerField(default=0)),
                ('draws', models.IntegerField(default=0)),
                ('strength', models.IntegerField(default=2000)),
                ('image', models.ImageField(upload_to='upload/')),
                ('country', models.CharField(default='()', max_length=264)),
            ],
        ),
        migrations.CreateModel(
            name='LE_group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264)),
                ('points', models.IntegerField(default=0)),
                ('scored', models.IntegerField(default=0)),
                ('conceded', models.IntegerField(default=0)),
                ('wins', models.IntegerField(default=0)),
                ('loses', models.IntegerField(default=0)),
                ('draws', models.IntegerField(default=0)),
                ('strength', models.IntegerField(default=2000)),
                ('image', models.ImageField(upload_to='upload/')),
                ('country', models.CharField(default='()', max_length=264)),
            ],
        ),
        migrations.CreateModel(
            name='LM_group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264)),
                ('points', models.IntegerField(default=0)),
                ('scored', models.IntegerField(default=0)),
                ('conceded', models.IntegerField(default=0)),
                ('wins', models.IntegerField(default=0)),
                ('loses', models.IntegerField(default=0)),
                ('draws', models.IntegerField(default=0)),
                ('strength', models.IntegerField(default=2000)),
                ('image', models.ImageField(upload_to='upload/')),
                ('country', models.CharField(default='()', max_length=264)),
            ],
        ),
        migrations.RemoveField(
            model_name='elim_ecl_1',
            name='conceded',
        ),
        migrations.RemoveField(
            model_name='elim_ecl_1',
            name='draws',
        ),
        migrations.RemoveField(
            model_name='elim_ecl_1',
            name='loses',
        ),
        migrations.RemoveField(
            model_name='elim_ecl_1',
            name='points',
        ),
        migrations.RemoveField(
            model_name='elim_ecl_1',
            name='scored',
        ),
        migrations.RemoveField(
            model_name='elim_ecl_1',
            name='wins',
        ),
        migrations.RemoveField(
            model_name='elim_ecl_2',
            name='conceded',
        ),
        migrations.RemoveField(
            model_name='elim_ecl_2',
            name='draws',
        ),
        migrations.RemoveField(
            model_name='elim_ecl_2',
            name='loses',
        ),
        migrations.RemoveField(
            model_name='elim_ecl_2',
            name='points',
        ),
        migrations.RemoveField(
            model_name='elim_ecl_2',
            name='scored',
        ),
        migrations.RemoveField(
            model_name='elim_ecl_2',
            name='wins',
        ),
        migrations.RemoveField(
            model_name='elim_ecl_3',
            name='conceded',
        ),
        migrations.RemoveField(
            model_name='elim_ecl_3',
            name='draws',
        ),
        migrations.RemoveField(
            model_name='elim_ecl_3',
            name='loses',
        ),
        migrations.RemoveField(
            model_name='elim_ecl_3',
            name='points',
        ),
        migrations.RemoveField(
            model_name='elim_ecl_3',
            name='scored',
        ),
        migrations.RemoveField(
            model_name='elim_ecl_3',
            name='wins',
        ),
        migrations.RemoveField(
            model_name='elim_ecl_4',
            name='conceded',
        ),
        migrations.RemoveField(
            model_name='elim_ecl_4',
            name='draws',
        ),
        migrations.RemoveField(
            model_name='elim_ecl_4',
            name='loses',
        ),
        migrations.RemoveField(
            model_name='elim_ecl_4',
            name='points',
        ),
        migrations.RemoveField(
            model_name='elim_ecl_4',
            name='scored',
        ),
        migrations.RemoveField(
            model_name='elim_ecl_4',
            name='wins',
        ),
        migrations.RemoveField(
            model_name='elim_le_3',
            name='conceded',
        ),
        migrations.RemoveField(
            model_name='elim_le_3',
            name='draws',
        ),
        migrations.RemoveField(
            model_name='elim_le_3',
            name='loses',
        ),
        migrations.RemoveField(
            model_name='elim_le_3',
            name='points',
        ),
        migrations.RemoveField(
            model_name='elim_le_3',
            name='scored',
        ),
        migrations.RemoveField(
            model_name='elim_le_3',
            name='wins',
        ),
        migrations.RemoveField(
            model_name='elim_le_4',
            name='conceded',
        ),
        migrations.RemoveField(
            model_name='elim_le_4',
            name='draws',
        ),
        migrations.RemoveField(
            model_name='elim_le_4',
            name='loses',
        ),
        migrations.RemoveField(
            model_name='elim_le_4',
            name='points',
        ),
        migrations.RemoveField(
            model_name='elim_le_4',
            name='scored',
        ),
        migrations.RemoveField(
            model_name='elim_le_4',
            name='wins',
        ),
        migrations.RemoveField(
            model_name='elim_lm_1',
            name='conceded',
        ),
        migrations.RemoveField(
            model_name='elim_lm_1',
            name='draws',
        ),
        migrations.RemoveField(
            model_name='elim_lm_1',
            name='loses',
        ),
        migrations.RemoveField(
            model_name='elim_lm_1',
            name='points',
        ),
        migrations.RemoveField(
            model_name='elim_lm_1',
            name='scored',
        ),
        migrations.RemoveField(
            model_name='elim_lm_1',
            name='wins',
        ),
        migrations.RemoveField(
            model_name='elim_lm_2',
            name='conceded',
        ),
        migrations.RemoveField(
            model_name='elim_lm_2',
            name='draws',
        ),
        migrations.RemoveField(
            model_name='elim_lm_2',
            name='loses',
        ),
        migrations.RemoveField(
            model_name='elim_lm_2',
            name='points',
        ),
        migrations.RemoveField(
            model_name='elim_lm_2',
            name='scored',
        ),
        migrations.RemoveField(
            model_name='elim_lm_2',
            name='wins',
        ),
        migrations.RemoveField(
            model_name='elim_lm_3',
            name='conceded',
        ),
        migrations.RemoveField(
            model_name='elim_lm_3',
            name='draws',
        ),
        migrations.RemoveField(
            model_name='elim_lm_3',
            name='loses',
        ),
        migrations.RemoveField(
            model_name='elim_lm_3',
            name='points',
        ),
        migrations.RemoveField(
            model_name='elim_lm_3',
            name='scored',
        ),
        migrations.RemoveField(
            model_name='elim_lm_3',
            name='wins',
        ),
        migrations.RemoveField(
            model_name='elim_lm_4',
            name='conceded',
        ),
        migrations.RemoveField(
            model_name='elim_lm_4',
            name='draws',
        ),
        migrations.RemoveField(
            model_name='elim_lm_4',
            name='loses',
        ),
        migrations.RemoveField(
            model_name='elim_lm_4',
            name='points',
        ),
        migrations.RemoveField(
            model_name='elim_lm_4',
            name='scored',
        ),
        migrations.RemoveField(
            model_name='elim_lm_4',
            name='wins',
        ),
        migrations.AddField(
            model_name='elim_ecl_1',
            name='country',
            field=models.CharField(default='()', max_length=264),
        ),
        migrations.AddField(
            model_name='elim_ecl_2',
            name='country',
            field=models.CharField(default='()', max_length=264),
        ),
        migrations.AddField(
            model_name='elim_ecl_3',
            name='country',
            field=models.CharField(default='()', max_length=264),
        ),
        migrations.AddField(
            model_name='elim_ecl_4',
            name='country',
            field=models.CharField(default='()', max_length=264),
        ),
        migrations.AddField(
            model_name='elim_le_3',
            name='country',
            field=models.CharField(default='()', max_length=264),
        ),
        migrations.AddField(
            model_name='elim_le_4',
            name='country',
            field=models.CharField(default='()', max_length=264),
        ),
        migrations.AddField(
            model_name='elim_lm_1',
            name='country',
            field=models.CharField(default='()', max_length=264),
        ),
        migrations.AddField(
            model_name='elim_lm_2',
            name='country',
            field=models.CharField(default='()', max_length=264),
        ),
        migrations.AddField(
            model_name='elim_lm_3',
            name='country',
            field=models.CharField(default='()', max_length=264),
        ),
        migrations.AddField(
            model_name='elim_lm_4',
            name='country',
            field=models.CharField(default='()', max_length=264),
        ),
    ]
