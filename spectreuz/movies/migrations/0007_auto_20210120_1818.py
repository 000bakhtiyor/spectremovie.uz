# Generated by Django 3.1.3 on 2021-01-20 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_auto_20210118_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='details',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='movies',
            name='genre',
            field=models.CharField(choices=[('1', 'Action'), ('2', 'Comedy'), ('3', 'Drama'), ('4', 'Fantasy'), ('5', 'Mystery'), ('6', 'Romance'), ('7', 'Horror'), ('8', 'Teen')], default='1', max_length=20),
        ),
        migrations.AlterField(
            model_name='slider',
            name='slider_image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]