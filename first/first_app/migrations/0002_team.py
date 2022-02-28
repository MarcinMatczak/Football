# Generated by Django 3.1.5 on 2021-03-20 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264)),
                ('points', models.IntegerField()),
                ('scored', models.IntegerField()),
                ('conceded', models.IntegerField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]