# Generated by Django 3.0.6 on 2020-06-03 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agg', '0010_auto_20200602_0142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estates',
            name='beds',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='estates',
            name='garages',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='estates',
            name='showers',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='estates',
            name='url',
            field=models.URLField(null=True),
        ),
    ]
