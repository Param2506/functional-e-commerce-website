# Generated by Django 4.0.4 on 2022-06-16 10:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_alter_product_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2022, 6, 16, 10, 50, 8, 990359, tzinfo=utc)),
        ),
    ]
