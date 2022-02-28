# Generated by Django 3.1.5 on 2021-03-25 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0013_auto_20210323_1618'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anglia',
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
            ],
        ),
        migrations.CreateModel(
            name='Francja',
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
            ],
        ),
        migrations.CreateModel(
            name='Hiszpania',
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
            ],
        ),
        migrations.CreateModel(
            name='Niemcy',
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
            ],
        ),
        migrations.CreateModel(
            name='Wlochy',
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
            ],
        ),
        migrations.RemoveField(
            model_name='druga_liga',
            name='last_conceded',
        ),
        migrations.RemoveField(
            model_name='druga_liga',
            name='last_scored',
        ),
        migrations.RemoveField(
            model_name='ekstraklasa',
            name='last_conceded',
        ),
        migrations.RemoveField(
            model_name='ekstraklasa',
            name='last_scored',
        ),
        migrations.RemoveField(
            model_name='pierwsza_liga',
            name='last_conceded',
        ),
        migrations.RemoveField(
            model_name='pierwsza_liga',
            name='last_scored',
        ),
    ]