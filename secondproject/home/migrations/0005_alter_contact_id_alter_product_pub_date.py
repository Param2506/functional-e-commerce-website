# Generated by Django 4.0.4 on 2022-06-14 07:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_contact_rename_description_product_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2022, 6, 14, 7, 46, 50, 46420, tzinfo=utc)),
        ),
    ]
