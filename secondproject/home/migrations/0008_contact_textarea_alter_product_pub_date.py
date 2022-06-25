# Generated by Django 4.0.4 on 2022-06-14 09:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_contact_name_alter_product_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='textarea',
            field=models.CharField(default='', max_length=400),
        ),
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2022, 6, 14, 9, 43, 42, 780551, tzinfo=utc)),
        ),
    ]