# Generated by Django 3.0.6 on 2020-06-02 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agg', '0009_auto_20200602_0141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estates',
            name='currency',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='estates',
            name='price',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='estates',
            name='rent_period',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='estates',
            name='time_posted',
            field=models.CharField(max_length=200, null=True),
        ),
    ]