# Generated by Django 2.2.16 on 2021-01-18 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20210118_0452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='slider_image',
            field=models.ImageField(upload_to='movies/static/images/'),
        ),
    ]
