# Generated by Django 3.1.5 on 2021-03-20 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Liga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264)),
                ('teams', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='first_app.team')),
            ],
        ),
    ]
