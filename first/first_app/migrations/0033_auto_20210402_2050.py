# Generated by Django 3.1.5 on 2021-04-02 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0032_ecl_gallery_le_gallery_lm_gallery_pol_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='PP_gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264)),
                ('image', models.ImageField(upload_to='upload/')),
            ],
        ),
        migrations.RemoveField(
            model_name='pol_gallery',
            name='country',
        ),
    ]
