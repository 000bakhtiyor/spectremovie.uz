# Generated by Django 2.2.16 on 2021-02-09 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20210131_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='poster',
            field=models.ImageField(default='/images/card.jfif', upload_to='posters/'),
        ),
    ]