# Generated by Django 3.0.6 on 2020-05-30 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agg', '0004_auto_20200530_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estates',
            name='beds',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='estates',
            name='garages',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='estates',
            name='showers',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
