# Generated by Django 4.0.4 on 2022-06-09 08:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Pub_date',
            field=models.DateField(default=datetime.datetime(2022, 6, 9, 13, 46, 56, 109330)),
        ),
        migrations.AlterField(
            model_name='product',
            name='Product_name',
            field=models.CharField(default='', max_length=20),
        ),
    ]
