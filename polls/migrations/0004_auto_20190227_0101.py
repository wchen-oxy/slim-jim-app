# Generated by Django 2.1.7 on 2019-02-27 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20190226_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='Calories',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='PrepTime',
            field=models.CharField(default='', max_length=10),
        ),
    ]