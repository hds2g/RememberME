# Generated by Django 3.2 on 2021-12-14 20:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remembers', '0007_auto_20211214_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remember',
            name='showing_date',
            field=models.DateField(default=datetime.datetime(2021, 12, 21, 20, 24, 35, 93706), verbose_name='Showing Date'),
        ),
        migrations.AlterField(
            model_name='remember',
            name='stage',
            field=models.CharField(choices=[('1 Week', '7'), ('2 Week', '14'), ('1 Month', '30'), ('2 Month', '60'), ('3 Month', '90'), ('6 Month', '180'), ('1 Year', '360')], default=('1 Week', '7'), max_length=10),
        ),
    ]