# Generated by Django 2.2.16 on 2021-02-09 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_auto_20210209_0319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='poster',
            field=models.ImageField(default='/card.jfif', upload_to='posters/'),
        ),
    ]
