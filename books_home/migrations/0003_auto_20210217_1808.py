# Generated by Django 2.2.13 on 2021-02-17 12:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_home', '0002_auto_20210215_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='book_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 17, 18, 8, 59, 111757)),
        ),
    ]
