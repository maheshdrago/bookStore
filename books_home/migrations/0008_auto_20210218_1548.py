# Generated by Django 2.2.13 on 2021-02-18 10:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_home', '0007_auto_20210218_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='category',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='book_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 18, 15, 48, 7, 699871)),
        ),
    ]
