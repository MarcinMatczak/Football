# Generated by Django 3.1.5 on 2021-04-02 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0031_ekstraklasa_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='ECL_gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264)),
                ('image', models.ImageField(upload_to='upload/')),
                ('country', models.CharField(default='()', max_length=264)),
            ],
        ),
        migrations.CreateModel(
            name='LE_gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264)),
                ('image', models.ImageField(upload_to='upload/')),
                ('country', models.CharField(default='()', max_length=264)),
            ],
        ),
        migrations.CreateModel(
            name='LM_gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264)),
                ('image', models.ImageField(upload_to='upload/')),
                ('country', models.CharField(default='()', max_length=264)),
            ],
        ),
        migrations.CreateModel(
            name='POL_gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264)),
                ('image', models.ImageField(upload_to='upload/')),
                ('country', models.CharField(default='()', max_length=264)),
            ],
        ),
    ]